from django.db import models

# Create your models here.
from django.db import models
from account.models import User

class Kategori(models.Model):
    namaKategori = models.TextField()
    deskripsi = models.CharField(max_length=1000)

class Toko(models.Model):
    idKategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    namaToko = models.TextField()
    deskripsi = models.CharField(max_length=1000)

class Produk(models.Model):
    idToko = models.ForeignKey(Toko, on_delete=models.CASCADE)
    namaProduk = models.TextField()
    deskripsi = models.CharField(max_length=1000)

class Favorites(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    tokoId = models.ForeignKey(Toko, on_delete=models.CASCADE)