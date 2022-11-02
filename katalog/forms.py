from django import forms
from django.forms import ModelForm
from addproduct.models import Product

class LikeForm(ModelForm):
    title = forms.IntegerField()

    class Meta:
        model = Product
        exclude = ('id_toko', 'name', 'nama_produk', 'kategori_produk', 'harga_produk', 'gambar_produk', 'deskripsi_produk', 'link_produk', 'is_valid')
        fields = ('like',)

