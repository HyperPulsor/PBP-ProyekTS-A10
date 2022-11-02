from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import SignUpBuyerForm, SignUpSellerForm, LoginForm, DonasiForm
from django.contrib.auth import authenticate, login, logout
import json
from addkategori.models import Kategori
from adminfaq.models import Faq

# Create your views here.

def donasi_barang(request):
    form = DonasiForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        barang = form.cleaned_data['input_barang']
        Donasi.objects.create(user=request.user, tipe=True, input_uang=0, input_barang=barang)
    return render (request, 'donasi.html')

def index(request):
    return render(request, 'index.html')

def registerbuyer(request):
    msg = None
    if request.method == 'POST':
        form = SignUpBuyerForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('account:login_view')
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
            return redirect('account:login_view')
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
                return redirect('account:adminpage')
            elif user is not None and user.is_buyer:
                login(request, user)
                return redirect('account:buyer')
            elif user is not None and user.is_seller:
                login(request, user)
                return redirect('account:seller')
            else:
                msg= 'Akun tidak ditemukan'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

def admin(request):
    kategori_item = Kategori.objects.all()
    context = {
        'kategori_item' : kategori_item,
    }
    return render(request,'show_admin.html', context)

def buyer(request):
    kategori_item = Kategori.objects.all()
    context = {
        'kategori_item' : kategori_item,
    }
    return render(request,'show_pembeli.html', context)

def seller(request):
    kategori_item = Kategori.objects.all()
    context = {
        'kategori_item' : kategori_item,
    }
    return render(request,'show_penjual.html', context)

def logout_user(request):
    logout(request)
    return redirect('account:index')