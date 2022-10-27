from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    nama_pemilik = models.CharField(max_length=50)
    id_pemilik = models.ForeignKey(to=User, on_delete=models.CASCADE)
    nama_project = models.CharField(max_length=50)
    kategori = models.CharField(max_length=50)
    bayaran = models.IntegerField()
    deskripsi = models.TextField()
    estimasi = models.CharField(max_length=30)
    skills = models.TextField()
    kontak_pemilik = models.TextField()
    jumlah_orang = models.IntegerField()
    acc = models.BooleanField(default=False)
    buka = models.BooleanField(default=True)

class MultiImage(models.Model):
    def default(self):
        return self.images.filter(default=True).first()
    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)
class Image(models.Model):
    name = models.CharField(max_length=255)
    model = models.ForeignKey(MultiImage, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)

class Product(MultiImage):
    name = models.CharField(max_length=255)
    nama_produk = models.CharField(max_length=255)
    kategori_produk = models.CharField(max_length=255)
    harga_produk = models.IntegerField()
    gambar_produk = models.ImageField()
    deskripsi_produk = models.CharField(max_length=255)
    link_produk = models.TextField()
    is_valid = models.BooleanField()




