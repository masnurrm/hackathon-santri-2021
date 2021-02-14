# Generated by Django 3.1 on 2021-02-12 22:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20210120_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='nomor_induk',
            field=models.CharField(default='1', max_length=50, unique=True, verbose_name='nomor induk'),
        ),
        migrations.CreateModel(
            name='Pengaduan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=128)),
                ('isi', models.CharField(max_length=256)),
                ('pengadu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pengadu', to=settings.AUTH_USER_MODEL, to_field='nomor_induk')),
            ],
        ),
    ]
