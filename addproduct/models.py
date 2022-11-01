from email.policy import default
from django.db import models
from account.models import User

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
    id_toko = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    nama_produk = models.CharField(max_length=255)
    kategori_produk = models.CharField(max_length=255)
    harga_produk = models.IntegerField()
    gambar_produk = models.ImageField()
    deskripsi_produk = models.CharField(max_length=255)
    link_produk = models.TextField()
    is_valid = models.BooleanField()




