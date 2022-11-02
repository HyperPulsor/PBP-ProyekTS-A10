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
    toko = toko_item = User.objects.get(id=id)
    context = {
        'toko':toko,
        'list_produk' : produk_item,
    }
    return render(request, "produk.html", context)

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