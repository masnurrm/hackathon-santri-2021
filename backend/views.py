from django.shortcuts import render
from rest_framework import viewsets

from .models import CustomUser, Laporan
from .serializers import CustomUserSerializer, LaporanSerializer

class LaporanViewset(viewsets.ModelViewSet):
    queryset = Laporan.objects.all()
    serializer_class = LaporanSerializer

class CustomUserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer