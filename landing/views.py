from urllib import response
from django.shortcuts import render
from landing.models import *
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
@login_required(login_url='/landing/login/')
def add_item_seller(request):
    if request.method == "POST":
        name = request.POST.get('item_name')
        description = request.POST.get('item_description')
        image = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(image.name, image)
        file_url = fss.url(file)
        # owner = Seller.objects.get(pk=request.session['seller_name'])
        owner = request.user.seller
        if name != "" and description != "":
            CardDisplay.objects.create(description=description, name=name, owner=owner, image=image, file_url=file_url)
            # allCards = CardDisplay.objects.filter(owner=owner)
            # context = {"allCards":allCards}
            # return render(request, "show.html", context)
            return redirect('landing:show_function')
        else:
            list(messages.get_messages(request))
            messages.error(request, "Harap Nama dan Deskripsi Barang")
    return render(request, "landing.html")

@login_required(login_url='/landing/login/')
def show_function(request):
    owner = request.user.seller
    allCards = CardDisplay.objects.filter(owner=owner)
    context = {"allCards":allCards}
    return render(request, "show.html", context)
        
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Seller.objects.create(user=user)
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('landing:login')
    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url='/landing/login/')
def show_item(request):
    return render(request, "show.html")

@login_required(login_url='/landing/login/')
def show_json(request):
    data = CardDisplay.objects.filter(owner=request.user.seller)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            seller_name = Seller.objects.get(user=user)
            request.session['seller_name'] = seller_name.pk
            request.session.set_expiry(900)
            return redirect('landing:add_item_seller')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('landing:login')

