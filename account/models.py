from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_buyer = models.BooleanField('Is buyer', default=False)
    is_seller = models.BooleanField('Is seller', default=False)