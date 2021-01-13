from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    nama = models.CharField(max_length=64, default="UnNamed")
    nomor_induk = models.CharField(_("nomor induk"), unique=True, max_length=50)
    telepon = models.CharField(max_length=13, unique=True)
    alamat = models.CharField(max_length=256)
    tanggal_lahir = models.CharField(max_length=16)
    penyakit_bawaan = models.CharField(max_length=64)

    USERNAME_FIELD = 'nomor_induk'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.nama

class Laporan(models.Model):
    id_pelapor = models.IntegerField(_("nomor induk pelapor"))
    id_dilaporkan = models.IntegerField(_("nomor induk dilaporkan"))
    keluhan = models.CharField(max_length=64)
    tanggal_laporan = models.CharField(max_length=16)
    status_laporan = models.CharField(max_length=32)
    asrama = models.CharField(max_length=8, default="Belum diatur")


