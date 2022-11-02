<<<<<<< HEAD
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
=======
from dataclasses import fields
from pyexpat import model
from django import forms
from account.models import Donasi
from django.contrib.auth.forms import UserCreationForm
from .models import User
from account import models

class DonasiForm(forms.ModelForm):
    class Meta:
        model = Donasi
        fields = ['input_uang', 'input_barang']
>>>>>>> 3141d3d85fd05be510a87837a2e96bda38670caf

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class SignUpBuyerForm(UserCreationForm):
    nama = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    class Meta:
        model = User
        fields = ('nama', 'username', 'email', 'password1', 'password2',
        'is_admin', 'is_buyer', 'is_seller')


class SignUpSellerForm(UserCreationForm):
    nama = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    namausaha = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    deskripsi = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    alamat = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    kontak = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    linktoko = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('nama', 'username', 'email', 'password1', 'password2', 'namausaha',
        'deskripsi', 'alamat', 'kontak', 'linktoko',
        'is_admin', 'is_buyer', 'is_seller')