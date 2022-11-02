from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_buyer = models.BooleanField('Is buyer', default=False)
    is_seller = models.BooleanField('Is seller', default=False)

class Donasi(models.Model):
    # True = Barang, False = Uang
    tipe = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_uang = models.PositiveIntegerField()
    input_barang = models.TextField()