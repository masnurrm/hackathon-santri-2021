from rest_framework import serializers

from .models import Laporan, CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'nama', 'nomor_induk', 'alamat', 'penyakit_bawaan', 'telepon', 'is_staff', 'is_superuser']

class LaporanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laporan
        fields = ['nomor_induk_pelapor', 'nomor_induk_dilaporkan', 'keluhan', 'tanggal_laporan', 'status_laporan', 'lapor_pusat']
