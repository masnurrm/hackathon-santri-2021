from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy

class CustomUserManager(BaseUserManager):

    def create_user(self, nomor_induk, password, **extra_fields):
        # if email is null
        if not nomor_induk:
            raise ValueError(ugettext_lazy("Nomor induk harus diisi"))

        user = self.model(nomor_induk=nomor_induk, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, nomor_induk, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is False:
            raise ValueError(ugettext_lazy("Superuser harus bernilai is_staff=True"))
        if extra_fields.get('is_superuser') is False:
            raise ValueError(ugettext_lazy("Superuser harus bernilai is_superuser=True"))
        
        return self.create_user(nomor_induk, password, **extra_fields)