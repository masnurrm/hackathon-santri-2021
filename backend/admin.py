from django.contrib import admin

from .models import CustomUser, Laporan
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Laporan)
