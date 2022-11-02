# Generated by Django 4.1 on 2022-10-29 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaKategori', models.TextField()),
                ('deskripsi', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Toko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaToko', models.TextField()),
                ('deskripsi', models.CharField(max_length=1000)),
                ('idKategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='katalog.kategori')),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaProduk', models.TextField()),
                ('deskripsi', models.CharField(max_length=1000)),
                ('idToko', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='katalog.toko')),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tokoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='katalog.toko')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
