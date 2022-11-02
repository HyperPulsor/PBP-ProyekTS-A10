from django.db import models
from django.contrib.auth.models import User

# https://medium.com/ibisdev/upload-multiple-images-to-a-model-with-django-fd00d8551a1c

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

class Product(models.Model):
    Makanan = 'Makanan'
    Pakaian = 'Pakaian'
    Perlengkapan_Rumah_Tangga = 'Perlengkapan Rumah Tangga'
    Otomotif = 'Otomotif'
    Alat_Tulis_Kantor = 'Alat Tulis Kantor'
    Kesehatan = 'Kesehatan'
    Kecantikan = 'Kecantikan'
    Alat_Musik = 'Alat Musik'
    Gadget = 'Gadget'
    Aksesoris = 'Aksesoris'
    Footwear = 'Footwear'
    Tas = 'Tas'


    Options_Kategori = [
        (Makanan, 'Makanan'),
        (Pakaian, 'Pakaian'),
        (Perlengkapan_Rumah_Tangga, 'Perlengkapan Rumah Tangga'),
        (Otomotif, 'Otomotif'),
        (Alat_Tulis_Kantor, 'Alat Tulis Kantor'),
        (Kesehatan,'Kesehatan'),
        (Kecantikan, 'Kecantikan'),
        (Alat_Musik, 'Alat Musik'),
        (Gadget, 'Gadget'),
        (Aksesoris, 'Aksesoris'),
        (Footwear, 'Footwear'),
        (Tas, 'Tas'),
        
    ]

    nama_produk = models.CharField(max_length=255)
    kategori_produk = models.CharField(
        max_length=255,
        choices=Options_Kategori,
        default=Makanan,
    )
    harga_produk = models.IntegerField()
    gambar_produk = models.ImageField(null = True, blank= True,upload_to = "addproduct/files/images/")
    deskripsi_produk = models.TextField()
    link_produk = models.TextField()
    is_valid = models.BooleanField()







