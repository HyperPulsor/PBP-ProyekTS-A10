from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect, JsonResponse
from django.http.response import HttpResponse
from account.forms import SignUpBuyerForm, SignUpSellerForm
from .forms import UpdateProfilBuyer, UpdateProfilSeller
# from django.http import JsonResponse
# from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
# from django.views.decorators.csrf import csrf_protect, csrf_exempt
# import json

# Create your views here.
def show_buyer(request):
    if not request.user.is_authenticated:
        return redirect("login/") 
    users = SignUpBuyerForm.objects.all().values()
    response = {'users':users}
    return render(request, 'buyer-profile.html', response)

def show_seller(request):
    if not request.user.is_authenticated:
        return redirect("login/") 
    users = SignUpSellerForm.objects.all().values()
    response = {'users':users}
    return render(request, 'seller-profile.html', response)

def validate_email_buyer(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': SignUpBuyerForm.objects.exclude(id = request.user.id).filter(email__iexact=email).exists()
    }
    return JsonResponse(data)

def validate_email_seller(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': SignUpSellerForm.objects.exclude(id = request.user.id).filter(email__iexact=email).exists()
    }
    return JsonResponse(data)

def edit_buyer(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login/") 
    user_id = request.user.id
    try:
        account = SignUpBuyerForm.objects.get(pk=user_id)
    except SignUpBuyerForm.DoesNotExist:
        return HttpResponse("Something went wrong")
    context = {}
    if request.POST:
        form = UpdateProfilBuyer(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('profile_handler/')
        else :
            form = UpdateProfilBuyer(request.POST, instance= request.user,       
                initial = {
                    "nama" : account.nama,
                    "username" : account.username,
                    "email" : account.email,
                    "password" : account.password
                }   
            )
            context['form'] = form
            validate_email_buyer(request)
    else :
        form = UpdateProfilBuyer(request.POST, instance= request.user,       
                initial = {
                    "nama" : account.nama,
                    "username" : account.username,
                    "email" : account.email,
                    "password" : account.password
                }   
            ) 
        context['form'] = form
    validate_email_buyer(request)
    return render(request, 'buyer-profile-edit.html', context)

def edit_seller(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login/") 
    user_id = request.user.id
    try:
        account = SignUpSellerForm.objects.get(pk=user_id)
    except SignUpSellerForm.DoesNotExist:
        return HttpResponse("Something went wrong")
    context = {}
    if request.POST:
        form = UpdateProfilSeller(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('profile_handler/')
        else :
            form = UpdateProfilSeller(request.POST, instance= request.user,       
                initial = {
                    "nama" : account.nama,
                    "username" : account.username,
                    "email" : account.email,
                    "password" : account.password,
                    "namausaha" : account.namausaha,
                    "deskripsi" : account.deskripsi,
                    "alamat" : account.alamat,
                    "kontak" : account.kontak,
                    "linktoko" : account.linktoko
                }   
            )
            context['form'] = form
            validate_email_seller(request)
    else :
        form = UpdateProfilSeller(request.POST, instance= request.user,       
                initial = {
                    "nama" : account.nama,
                    "username" : account.username,
                    "email" : account.email,
                    "password" : account.password,
                    "namausaha" : account.namausaha,
                    "deskripsi" : account.deskripsi,
                    "alamat" : account.alamat,
                    "kontak" : account.kontak,
                    "linktoko" : account.linktoko
                }   
            ) 
        context['form'] = form
    validate_email_seller(request)
    return render(request, 'seller-profile-edit.html', context)