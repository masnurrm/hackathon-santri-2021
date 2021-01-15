from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse

from .models import CustomUser, Laporan
from .serializers import CustomUserSerializer, LaporanSerializer

def index(request):
    return HttpResponse("Halo halo")

class LaporanViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Laporan.objects.all()
    serializer_class = LaporanSerializer

class LaporanList(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        laporan = Laporan.objects.all()
        serializer = LaporanSerializer(laporan, many=True)
        return Response(serializer.data)
    def post(self, request):
        request['nomor_induk'] = request.user.nomor_induk
        serializer = LaporanSerializer(data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LaporanDetail(APIView):

    permission_classes = [permissions.IsAuthenticated]
    
    def get_laporan(self, pk):
        try:
            return Laporan.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk):
        laporan = self.get_laporan(pk)
        serializer = LaporanSerializer(laporan)
        return Response(serializer.data)

class CustomUserViewset(viewsets.ModelViewSet):
    
    permission_classes = [permissions.IsAuthenticated]
    
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserDetail(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    
    def get_user(self, nomor_induk):
        try:
            return CustomUser.objects.get(nomor_induk=nomor_induk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, nomor_induk):
        user = self.get_user(nomor_induk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

class CustomUserList(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
