from django.db import models

# Create your models here.
class Faq(models.Model):
    question = models.TextField(max_length=100,blank=True)
    answer = models.TextField(blank=True)
