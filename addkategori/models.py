from django.db import models
from django.conf import settings

# Create your models here.
class Kategori(models.Model):
    # user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    nama = models.CharField(max_length=50)
    deskripsi = models.TextField(max_length=150) 
    gambar = models.ImageField(null=True, blank=True)
    file_url = models.TextField(null=True, blank=True)