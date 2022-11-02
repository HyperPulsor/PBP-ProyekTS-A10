<<<<<<< HEAD
from django.shortcuts import render, redirect
from .forms import SignUpBuyerForm, SignUpSellerForm, LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.

=======
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import SignUpBuyerForm, SignUpSellerForm, LoginForm, DonasiForm
from django.contrib.auth import authenticate, login, logout
import json
from addkategori.models import Kategori

# Create your views here.

def donasi_barang(request):
    form = DonasiForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        barang = form.cleaned_data['input_barang']
        Donasi.objects.create(user=request.user, tipe=True, input_uang=0, input_barang=barang)
    return render (request, 'donasi.html')
>>>>>>> 3141d3d85fd05be510a87837a2e96bda38670caf

def index(request):
    return render(request, 'index.html')

def registerbuyer(request):
    msg = None
    if request.method == 'POST':
        form = SignUpBuyerForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
<<<<<<< HEAD
            return redirect('login_view')
=======
            return redirect('account:login_view')
>>>>>>> 3141d3d85fd05be510a87837a2e96bda38670caf
        else:
            msg = 'form is not valid'
    else:
        form = SignUpBuyerForm()
    return render(request,'registerbuyer.html', {'form': form, 'msg': msg})

def registerseller(request):
    msg = None
    if request.method == 'POST':
        form = SignUpSellerForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
<<<<<<< HEAD
            return redirect('login_view')
=======
            return redirect('account:login_view')
>>>>>>> 3141d3d85fd05be510a87837a2e96bda38670caf
        else:
            msg = 'form is not valid'
    else:
        form = SignUpSellerForm()
    return render(request,'registerseller.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
<<<<<<< HEAD
                return redirect('adminpage')
            elif user is not None and user.is_buyer:
                login(request, user)
                return redirect('buyer')
            elif user is not None and user.is_seller:
                login(request, user)
                return redirect('seller')
=======
                return redirect('account:adminpage')
            elif user is not None and user.is_buyer:
                login(request, user)
                return redirect('account:buyer')
            elif user is not None and user.is_seller:
                login(request, user)
                return redirect('account:seller')
>>>>>>> 3141d3d85fd05be510a87837a2e96bda38670caf
            else:
                msg= 'Akun tidak ditemukan'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

<<<<<<< HEAD

def admin(request):
    return render(request,'admin.html')


def buyer(request):
    return render(request,'buyer.html')


def seller(request):
    return render(request,'seller.html')
=======
def admin(request):
    return render(request,'show_admin.html')

def buyer(request):
    kategori_item = Kategori.objects.all()
    context = {
        'kategori_item' : kategori_item,
    }
    return render(request,'show_pembeli.html', context)

def seller(request):
    return render(request,'show_penjual.html')

def logout_user(request):
    logout(request)
    return redirect('account:index')
>>>>>>> 3141d3d85fd05be510a87837a2e96bda38670caf
