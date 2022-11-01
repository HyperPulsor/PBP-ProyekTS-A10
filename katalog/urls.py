from django.urls import path
from katalog.views import *

app_name = 'katalog'
urlpatterns = [
    path('show_produk/<int:id>/', show_produk_html_1, name='show_produk_detail'),
    path('show_toko/<str:nama>/<str:deskripsi>/', show_toko_html_1, name='show_toko_kategori'),
    path("show-json-produk/<int:id>/", show_json_produk, name='show-json-produk'),
    path("like/<str:nama_produk>/", like_ajax_submit, name = "like")
]