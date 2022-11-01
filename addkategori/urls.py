from django.urls import path
from addkategori.views import *

app_name = 'kategori'

urlpatterns = [
    path('', show_kategori, name='show_kategori'),
    path('create_kategori/', create_kategori, name='create_kategori'),
    path('delete_kategori/<int:id>/', delete_kategori, name='delete_kategori'),
]