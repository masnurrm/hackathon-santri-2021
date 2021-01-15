from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView


from .models import CustomUser, Laporan
from .serializers import CustomUserSerializer, LaporanSerializer

def index(request):
    return HttpResponse("Halo halo")


class LaporanViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Laporan.objects.all()
    serializer_class = LaporanSerializer


class CustomUserViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MyTokenObtainPairSerializer