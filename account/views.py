from django.shortcuts import render, redirect
from .forms import SignUpBuyerForm, SignUpSellerForm, LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.


def index(request):
    return render(request, 'index.html')

def registerbuyer(request):
    msg = None
    if request.method == 'POST':
        form = SignUpBuyerForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
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
            return redirect('login_view')
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
                return redirect('adminpage')
            elif user is not None and user.is_buyer:
                login(request, user)
                return redirect('buyer')
            elif user is not None and user.is_seller:
                login(request, user)
                return redirect('seller')
            else:
                msg= 'Akun tidak ditemukan'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')


def buyer(request):
    return render(request,'buyer.html')


def seller(request):
    return render(request,'seller.html')