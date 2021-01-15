from rest_framework import serializers

from .models import Laporan, CustomUser, RiwayatPenyakit

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'nama', 'nomor_induk', 'alamat', 'penyakit_bawaan', 'telepon', 'is_staff', 'is_superuser']

class LaporanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laporan
        fields = ['pelapor', 'dilaporkan', 'keluhan', 'tanggal_laporan', 'status_laporan', 'lapor_pusat']
        depth = 1

class RiwayatPenyakitSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiwayatPenyakit
        fields = '__all__'