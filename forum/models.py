#from tkinter import CASCADE
#from unittest.util import _MAX_LENGTH
from django.db import models
#from django.contrib.auth.models import User
from account.models import User

#class Author(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ForumUMKM(models.Model):
    title = models.CharField(max_length=100)
    discussion = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    #jangan lupa ganti user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username=models.CharField(max_length=50)
    #user = models.IntegerField()
    kategori = models.CharField(max_length=100)

class Replies(models.Model):
    discussion = models.TextField()
    #jangan lupa ganti user
    #user = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username=models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    forum = models.ForeignKey(ForumUMKM, on_delete=models.CASCADE)
