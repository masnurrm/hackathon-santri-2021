from rest_framework import serializers

from .models import Laporan, CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'nama', 'nomor_induk', 'alamat', 'penyakit_bawaan', 'telepon']

class LaporanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laporan
        fields = ['id_pelapor', 'id_dilaporkan', 'keluhan', 'tanggal_laporan', 'status_laporan']