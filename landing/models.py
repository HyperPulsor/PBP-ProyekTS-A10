from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True)

class CardDisplay(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Seller, on_delete=models.CASCADE,blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    file_url = models.TextField(blank=True,null=True)
