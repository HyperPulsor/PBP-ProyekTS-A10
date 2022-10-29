from http.client import HTTPResponse
from django.shortcuts import render
from katalog.models import Toko, Produk, Favorites
from account.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# @login_required(login_url='/account/login/')
# pass nama dan deskripsi kategori
# request[?] -> Kategori
def show_toko_html(request):
    #kategori = dari request
    #deskripsi Kategori dari request
    toko_item = Toko.objects.all()
    context = {
        'list_toko' : toko_item,
    }
    return render(request, "toko.html", context)

def show_produk_html(request):
    produk_item = Produk.objects.filter(idToko=1) #id toko dari request
    context = {
        'list_produk' : produk_item,
    }
    return render(request, "produk.html", context)

#userid 7 tokoId dari request
def add_favorites(request):
    user_id = User.objects.get(id=1) #diganti pakai request
    toko_id = Toko.objects.get(id=3)
    new_favorites = Favorites.objects.create(userId=user_id, tokoId=toko_id)
    return HttpResponseRedirect('/katalog/show_toko')
    

#userid dari request
def show_favorites_html(request):
    user_id = 1 #diganti pakai request
    favorites = Favorites.objects.filter(userId=user_id)
    toko_favorite = []
    
    for favorite in favorites:
        toko_favorite.append(favorite.tokoId.id)

    toko_item = Toko.objects.filter(id__in=toko_favorite)
    context = {
        'list_toko' : toko_item,
    }
    return render(request, "favorites.html", context)