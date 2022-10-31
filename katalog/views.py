from http.client import HTTPResponse
from django.shortcuts import render
from addproduct.models import Product
from katalog.models import Toko, Produk, Favorites
from account.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# @login_required(login_url='/account/login/')
# pass nama dan deskripsi kategori
# request[?] -> Kategori
def show_toko_html(request):
    # kategori = request.kategori #pass kategori ke request
    # deskripsi_kategori = request.deskripsi_kategori #pass deskripsi_kategori ke request
    toko_item = User.objects.filter(User.is_seller)
    # toko_item = Toko.objects.all()
    context = {
        # 'kategori' : kategori,
        # 'deskripsi_kategori' : deskripsi_kategori,
        'list_toko' : toko_item,
    }
    return render(request, "toko.html", context)

def show_produk_html(request):
    produk_item = Produk.objects.filter(idToko=request.user.id) #id toko dari request
    context = {
        'list_produk' : produk_item,
    }
    return render(request, "produk.html", context)

def show_produk_html_addproduct_model(request):
    # produk_item = Produk.objects.filter(idToko=request.user.id) #id toko dari request
    produk_item = Product.objects.filter(idToko=request.user.id) #id toko dari request
    context = {
        'list_produk' : produk_item,
    }
    return render(request, "produk.html", context)