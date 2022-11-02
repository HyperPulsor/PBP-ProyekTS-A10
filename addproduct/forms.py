from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class AddProductForm(forms.ModelForm):
    nama_produk = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id":"nama_produk",
            }
        )
    )

    kategori_produk = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id":"kategori_produk",
            }
        )
    )

    # CHOICES = (('Makanan', 'Makanan'),
    #     ('Pakaian', 'Pakaian'),
    #     ('Perlengkapan Rumah Tangga', 'Perlengkapan Rumah Tangga'),
    #     ('Otomotif', 'Otomotif'),
    #     ('Alat Tulis Kantor', 'Alat Tulis Kantor'),
    #     ('Kesehatan','Kesehatan'),
    #     ('Kecantikan', 'Kecantikan'),
    #     ('Alat Musik', 'Alat Musik'),
    #     ('Gadget', 'Gadget'),
    #     ('Aksesoris', 'Aksesoris'),
    #     ('Footwear', 'Footwear'),
    #     ('Tas', 'Tas'),)
    # kategori_produk = forms.ChoiceField(
    #     widget=forms.Select(
    #         attrs={
    #             "class": "form-select",
    #             "id":"kategori_produk",
    #         }
    #     ),
    #     choices=CHOICES
    # )

    harga_produk  = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "id":"harga_produk"
            }
        )
    )

    gambar_produk = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id":"gambar_produk"
            }
        )
    )

    deskripsi_produk  = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id":"deskripsi_produk"
            }
        )
    )

    link_produk  = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id":"link_produk"
            }
        )
    )

    
    class Meta:
        model = Product
        fields = ('nama_produk', 'kategori_produk', 'harga_produk', 'gambar_produk', 'deskripsi_produk', 'link_produk',)


