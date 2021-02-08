from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Laporan, CustomUser, RiwayatPenyakit

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'nama', 'nomor_induk', 'alamat', 'penyakit_bawaan', 'telepon', 'is_staff', 'is_superuser']

class LaporanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laporan
        fields = ['id', 'pelapor', 'dilaporkan', 'keluhan', 'tanggal_laporan', 'status_laporan', 'lapor_pusat']
    
    def to_representation(self, instance):
        self.fields['pelapor'] =  CustomUserSerializer(read_only=True)
        self.fields['dilaporkan'] =  CustomUserSerializer(read_only=True)
        return super(LaporanSerializer, self).to_representation(instance)

class RiwayatPenyakitSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiwayatPenyakit
        fields = '__all__'

class CustomTOPS(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        serializer = CustomUserSerializer(user)
        token['user'] = serializer.data

        return token