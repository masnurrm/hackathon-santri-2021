from django.shortcuts import render
from django.core import exceptions
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .tasks import laporkan_pusat
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
import json

from .models import CustomUser, Laporan, RiwayatPenyakit, Pengaduan
from .serializers import CustomUserSerializer, LaporanSerializer, RiwayatPenyakitSerializer, CustomTOPS, PasswordResetSerializer, PengaduanSerializer

def index(request):
    return HttpResponse("Halo halo")

class LaporanListView(APIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        laporan = Laporan.objects.all()
        serializer = LaporanSerializer(laporan, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LaporanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(pelapor=request.user)
            laporkan_pusat.delay(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LaporanUpdateView(APIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_laporan(self, pk):
        try:
            return Laporan.objects.get(pk=pk)
        except exceptions.ObjectDoesNotExist:
            data = {}
            data['response'] = 'Laporan tidak ditemukan'
            return Response(data, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        laporan = self.get_laporan(pk)
        if request.user.is_staff:
            laporan.status_laporan = "Menunggu konfirmasi santri"
            laporan.save()
            serializer = LaporanSerializer(laporan)
            return Response(serializer.data)
        if request.user.is_staff is False:
            laporan.status_laporan = "Telah Ditangani"
            laporan.save()
            serializer = LaporanSerializer(laporan)
            return Response(serializer.data)

class LaporanDetailUserView(APIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_all_laporan(self, nomor_induk):
        try:
            return Laporan.objects.filter(pelapor=nomor_induk)
        except exceptions.ObjectDoesNotExist:
            data = {}
            data['response'] = 'Laporan tidak ditemukan'
            return Response(data, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        laporan = self.get_all_laporan(request.user.nomor_induk)
        serializer = LaporanSerializer(laporan, many=True)
        return Response(serializer.data)

class LaporanDetailIdView(APIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_detail_laporan(self, pk):
        try:
            return Laporan.objects.get(id=pk)
        except exceptions.ObjectDoesNotExist:
            data = {}
            data['response'] = 'Laporan tidak ditemukan'
            return Response(data, status=status.HTTP_404_NOT_FOUND)
    def get(self, request, pk):
        laporan = self.get_detail_laporan(pk)
        serializer = LaporanSerializer(laporan)
        return Response(serializer.data)

class LaporanUpdatePusatView(APIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_laporan(self, pk):
        try:
            return Laporan.objects.get(pk=pk)
        except exceptions.ObjectDoesNotExist:
            err = {'error':'Laporan tidak ditemukan'}
            err_message = json.dump(err)
            return Response(err_message, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        laporan = self.get_laporan(pk)
        if request.user.is_staff:
            laporan.lapor_pusat = True
            laporan.save()
            serializer = LaporanSerializer(laporan)
            return Response(serializer.data)

class RiwayatPenyakitDetailView(APIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_user(self, nomor_induk):
        try:
            return CustomUser.objects.get(nomor_induk=nomor_induk)
        except exceptions.ObjectDoesNotExist:
            data = {}
            data['response'] = 'User tidak ditemukan'
            return Response(data, status=status.HTTP_404_NOT_FOUND)
    def get_riwayat(self, nomor_induk):
        try:
            user_dilaporkan = self.get_user(nomor_induk)
            return RiwayatPenyakit.objects.filter(dilaporkan=user_dilaporkan)
        except exceptions.ObjectDoesNotExist:
            data = {}
            data['response'] = 'Riwayat tidak ditemukan'
            return Response(data, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, nomor_induk):
        riwayat = self.get_riwayat(nomor_induk)
        serializer = RiwayatPenyakitSerializer(riwayat, many=True)
        return Response(serializer.data)

class RiwayatPenyakitCreateView(APIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_dilaporkan(self, nomor_induk):
        try:
            return CustomUser.objects.get(nomor_induk=nomor_induk)
        except exceptions.ObjectDoesNotExist:
            data = {}
            data['response'] = 'User tidak ditemukan'
            return Response(data, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request, nomor_induk):
        dilaporkan = self.get_dilaporkan(nomor_induk)
        serializer = RiwayatPenyakitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(dilaporkan=dilaporkan)
            return Respone(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class CustomUserDetail(APIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_user(self, nomor_induk):
        try:
            return CustomUser.objects.get(nomor_induk=nomor_induk)
        except exceptions.ObjectDoesNotExist:
            data = {}
            data['response'] = 'User tidak ditemukan'
            return Response(data, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, nomor_induk):
        user = self.get_user(nomor_induk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

class CustomUserList(APIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

class CustomTOPV(TokenObtainPairView):
    serializer_class = CustomTOPS

class PasswordResetEmail(APIView):
    def get_user(self, nomor_induk):
        try:
            return CustomUser.objects.get(nomor_induk=nomor_induk)
        except exceptions.ObjectDoesNotExist:
            err = {'error':'user tidak ditemukan'}
            err_message = json.dump(err)
            return Response(err_message, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            nomor_induk = serializer.data['nomor_induk']
            data = {}
            user = self.get_user(nomor_induk=nomor_induk)
            subject = "Password Reset Requested"
            email_template_name = r"passwordResetEmail.txt"
            c = {
            "email":user.email,
            'domain':'127.0.0.1:8000',
            'site_name': 'Website',
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "user": user,
            'token': default_token_generator.make_token(user),
            'protocol': 'http',
            }
            email = render_to_string(email_template_name, c)
            try:
                send_mail(subject, email, 'santrisehat2020@gmail.com' , [user.email], fail_silently=False)
                data['response'] = True
                return Response(data, status=status.HTTP_200_OK)
            except BadHeaderError:
                data['response'] = False
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

# class ListPengaduanView(APIView):
#     authentication_classes = [authentication.JWTAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):
#         pengaduan = Pengaduan.objects.all()
#         serializer = PengaduanSerializer(pengaduan, many=True)
#         return Response(serializer.data)

# class DeletePengaduanView(APIView):
#     def get_pengaduan_object()

class PasswordReset(APIView):
    def get_user_object(self, uidb64):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None
        return user

    def post(self, request):
        user = self.get_user_object(request.data.get('uidb64'))
        token = request.data.get('token')
        data = {}

        if user is not None and default_token_generator.check_token(user, token):
            user.set_password(request.data.get('new_password'))
            user.save()
            data['response'] = True
            return Response(data)
        data['response'] = False
        return Response(data)
