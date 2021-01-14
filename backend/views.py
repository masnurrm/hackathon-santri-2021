from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import CustomUser, Laporan
from .serializers import CustomUserSerializer, LaporanSerializer

class LaporanViewset(viewsets.ModelViewSet):
    queryset = Laporan.objects.all()
    serializer_class = LaporanSerializer
    permission_classes = [permissions.IsAuthenticated]

class CustomUserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer