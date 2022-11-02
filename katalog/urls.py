from django.urls import path
from katalog.views import *

app_name = 'katalog'
urlpatterns = [
    path('show_produk/', show_produk_html, name='show_produk'),
    path('show_toko/', show_toko_html, name='show_toko'),
    path('add_favorites/', add_favorites, name='add_favorites'),
    path('show_favorites/', show_favorites_html, name='show_favorites'),
]