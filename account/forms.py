from dataclasses import fields
from pyexpat import model
from django import forms
from account.models import Donasi
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "email", 
            "password1", 
            "password2", 
        )

class BuyerSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "name", 
            "email", 
            "username", 
            "password1", 
            "password2", )
        
class SellerSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "name", 
            "email", 
            "password1", 
            "password2", 
            "namausaha",
            "kategori",
            "deskripsi", 
            "address",
            "kontak",
            "linktoko")