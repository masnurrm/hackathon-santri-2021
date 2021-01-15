from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import generics

from .models import CustomUser, Laporan, RiwayatPenyakit
from .serializers import CustomUserSerializer, LaporanSerializer, RiwayatPenyakitSerializer

def index(request):
    return HttpResponse("Halo halo")

class LaporanViewset(viewsets.ModelViewSet):
    serializer_class = LaporanSerializer
    queryset = Laporan.objects.all()

    def perform_create(self, serializer):
        serializer.save(pelapor=self.request.user)

class RiwayatPenyakitViewset(viewsets.ModelViewSet):
    serializer_class = RiwayatPenyakitSerializer
    queryset = RiwayatPenyakit.objects.all()

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
