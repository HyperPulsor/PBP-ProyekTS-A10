<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
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
    produk_item = Produk.objects.filter(idToko=1,is_valid=True) #id toko dari request
=======
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from addproduct.models import Product
from account.models import User
from django.contrib.auth.decorators import login_required
from django.core import serializers
from .forms import LikeForm

@login_required(login_url='/index/')
def show_toko_html_1(request, nama, deskripsi):
    toko_item = User.objects.filter(is_seller=True)
    tokos = []
    for obj in toko_item:
        id = obj._meta.get_field('id')
        nama_toko = obj._meta.get_field('username')
        email = obj._meta.get_field('email')
        field_id= id.value_from_object(obj)
        field_nama = nama_toko.value_from_object(obj)
        field_email = email.value_from_object(obj)
        print(email.value_from_object(obj))
        dict = { "id":field_id, "nama_toko": field_nama, "email":field_email}
        tokos.append(dict)

    context = {
        # 'kategori' : request.kategori_nama, -> ambil dr req but how
        'tokos': tokos,
        'list_toko' : toko_item,
        'kategori' : nama,
        'deskripsi': deskripsi,
    }
    return render(request, "toko.html", context)

@login_required(login_url='/index/')
def show_produk_html_1(request, id):
    produk_item = Product.objects.filter(id_toko=id) #id toko dari request
>>>>>>> 3141d3d85fd05be510a87837a2e96bda38670caf
    context = {
        'list_produk' : produk_item,
    }
    return render(request, "produk.html", context)

<<<<<<< HEAD
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
=======
def show_json_produk(request, id):
    produk_item = Product.objects.filter(id_toko=id) 
    return HttpResponse(serializers.serialize("json", produk_item), content_type="application/json")

@login_required(login_url='/todolist/login/')
def like_ajax_submit(request, nama_produk):
    if (request.method == "POST"):
        form = LikeForm(request.POST or None)
        if (form.is_valid()):
            user = request.user
            product = Product.objects.filter(nama_produk=nama_produk)
            like = product._meta.get_field('like')+1
            product.update(like=like)
            return JsonResponse({'like':like,})
>>>>>>> 3141d3d85fd05be510a87837a2e96bda38670caf
