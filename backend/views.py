from django.shortcuts import render
from django.core import exceptions
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from rest_framework_simplejwt import authentication
from django.http import HttpResponse
from .tasks import laporkan_pusat
import json

from .models import CustomUser, Laporan, RiwayatPenyakit
from .serializers import CustomUserSerializer, LaporanSerializer, RiwayatPenyakitSerializer

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
            # laporkan_pusat.delay(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LaporanUpdateView(APIView):
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
            err = {'error':'Laporan tidak ditemukan'}
            err_message = json.dump(err)
            return Response(err_message, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        laporan = self.get_laporan(request.user.nomor_induk)
        serializer = LaporanSerializer(laporan, many=True)
        return Response(serializer.data)

class LaporanDetailIdView(APIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_detail_laporan(self, pk):
        try:
            return Laporan.objects.get(id=pk)
        except exceptions.ObjectDoesNotExist:
            err = {'error':'Laporan tidak ditemukan'}
            err_message = json.dump(err)
            return Response(err_message, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        laporan = self.get_detail_laporan(pk)
        serializer = LaporanSerializer(laporan)
        return Response(serializer.data)

class RiwayatPenyakitDetailView(APIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_user(self, nomor_induk):
        try:
            return CustomUser.objects.get(nomor_induk=nomor_induk)
        except exceptions.ObjectDoesNotExist:
            err = {'error':'Laporan tidak ditemukan'}
            err_message = json.dump(err)
            return Response(err_message, status=status.HTTP_404_NOT_FOUND)  

    def get_riwayat(self, nomor_induk):
        try:
            user_dilaporkan = self.get_user(nomor_induk)
            return RiwayatPenyakit.objects.filter(dilaporkan=user_dilaporkan)
        except exceptions.ObjectDoesNotExist:
            err = {'error':'Laporan tidak ditemukan'}
            err_message = json.dump(err)
            return Response(err_message, status=status.HTTP_404_NOT_FOUND)

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
            err = {'error':'User tidak ditemukan'}
            err_message = json.dump(err)
            return Response(err_message, status=status.HTTP_404_NOT_FOUND)
    
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
            err = {'error':'Laporan tidak ditemukan'}
            err_message = json.dump(err)
            return Response(err_message, status=status.HTTP_404_NOT_FOUND)

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
