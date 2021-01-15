from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import CustomUser, Laporan
from .serializers import CustomUserSerializer, LaporanSerializer


class LaporanViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Laporan.objects.all()
    serializer_class = LaporanSerializer


class CustomUserViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
