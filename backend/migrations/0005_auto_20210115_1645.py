# Generated by Django 3.1 on 2021-01-15 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_laporan_lapor_pusat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laporan',
            old_name='id_dilaporkan',
            new_name='nomor_induk_dilaporkan',
        ),
        migrations.RenameField(
            model_name='laporan',
            old_name='id_pelapor',
            new_name='nomor_induk_pelapor',
        ),
    ]
