from django import forms

class FormKategori(forms.Form):
   nama = forms.CharField(label='Nama Kategori', widget=forms.TextInput(attrs={'placeholder': 'Kategori Baru'}))
   deskripsi = forms.CharField(label='Deskripsi Kategori', widget=forms.Textarea(attrs={'placeholder': 'Deskripsi Kategori'}))
   gambar = forms.ImageField()
   file_url = forms.CharField()