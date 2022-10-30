from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Faq(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    question = models.TextField(max_length=100,blank=True)
    answer = models.TextField(blank=True)
