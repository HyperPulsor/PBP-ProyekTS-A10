from django.urls import path
from katalog.views import *

app_name = 'katalog'
urlpatterns = [
<<<<<<< HEAD
    path('show_produk/', show_produk_html, name='show_produk'),
    path('show_toko/', show_toko_html, name='show_toko'),
    path('add_favorites/', add_favorites, name='add_favorites'),
    path('show_favorites/', show_favorites_html, name='show_favorites'),
=======
    path('show_produk/<int:id>/', show_produk_html_1, name='show_produk_detail'),
    path('show_toko/<str:nama>/<str:deskripsi>/', show_toko_html_1, name='show_toko_kategori'),
    path("show-json-produk/<int:id>/", show_json_produk, name='show-json-produk'),
    path("like/<str:nama_produk>/", like_ajax_submit, name = "like")
>>>>>>> 3141d3d85fd05be510a87837a2e96bda38670caf
]