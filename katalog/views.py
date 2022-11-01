from django.shortcuts import render
from addproduct.models import Product
from account.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required

@login_required(login_url='/index/')
def show_toko_html(request):
    toko_item = User.objects.filter(is_seller=True)
    # toko_item = Toko.objects.all()
    context = {
        # 'kategori' : request.kategori_nama, -> ambil dr req but how
        'list_toko' : toko_item,
    }
    return render(request, "toko.html", context)

@login_required(login_url='/index/')
def show_produk_html(request):
    produk_item = Product.objects.filter(id=request.idtoko) #id toko dari request
    context = {
        'list_produk' : produk_item,
    }
    return render(request, "produk.html", context)