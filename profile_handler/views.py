from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect, JsonResponse
from django.http.response import HttpResponse
from account.forms import SignUpBuyerForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic

from account.forms import *

from .forms import *

from profile_handler.models import Profile
from account.models import User

# Create your views here.
# def show_buyer(request):
#     # form= SignUpBuyerForm(request.POST or None)
#     # nama = ''
#     # if form.is_valid():
#     #     nama= form.cleaned_data.get("nama")

#     # context= {'form': form, 'nama': nama}
        
#     # return render(request, 'buyer-profile.html', context)

#     # if request.method == 'POST':
#     #     form = SignUpBuyerForm(request.POST)
#     #     if form.is_valid():
#     #         form_data = form.cleaned_data
#     #         obj = User()
#     #         obj.nama = form_data.get("nama")
#     #         # other fields
#     #         obj.save()
#     #         # return or redirect
#     # else:
#     #     form = SignUpBuyerForm()
#     # return render(request, 'buyer-profile.html', {'form': form})
#     # if not request.user.is_authenticated:
#     #     return redirect("login/") 
#     users = User.objects.all().values()
#     response = {'users':users}
#     return render(request, 'buyer-profile.html', response)

@login_required(login_url='/account/login/')
def show_profile(request):
    if not request.user.is_authenticated:
        return redirect("account/login/") 
    # user = User.objects.all().values()
    if request.user is not None and request.user.is_buyer:
                return redirect('showbuyer/')
    elif request.user is not None and request.user.is_seller:
                return redirect('showseller/')
    # response = {'user':user}

def show_buyer(request):
    return render(request,'buyer-profile.html')

def show_seller(request):
    return render(request,'seller-profile.html')

class BuyerEditView(generic.UpdateView):
    form_class = BuyerEditProfileForm
    template_name = 'buyer-profile-edit.html'
    success_url = reverse_lazy('profile:showbuyer')

    def get_object(self):
        return self.request.user

class SellerEditView(generic.UpdateView):
    form_class = SellerEditProfileForm
    template_name = 'seller-profile-edit.html'
    success_url = reverse_lazy('profile:showseller')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('profile:password_success')

def password_success(request):
    return render(request, 'password-success.html', {})

# def validate_email_buyer(request):
#     email = request.GET.get('email', None)
#     data = {
#         'is_taken': User.objects.exclude(id = request.user.id).filter(email__iexact=email).exists()
#     }
#     return JsonResponse(data)

# def validate_email_seller(request):
#     email = request.GET.get('email', None)
#     data = {
#         'is_taken': User.objects.exclude(id = request.user.id).filter(email__iexact=email).exists()
#     }
#     return JsonResponse(data)

# def edit_buyer(request, *args, **kwargs):
#     if not request.user.is_authenticated:
#         return redirect("login/") 
#     user_id = request.user.id
#     try:
#         account = User.objects.get(pk=user_id)
#     except User.DoesNotExist:
#         return HttpResponse("Something went wrong")
#     context = {}
#     if request.POST:
#         form = UpdateProfilBuyer(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('')
#         else :
#             form = UpdateProfilBuyer(request.POST, instance= request.user,       
#                 initial = {
#                     # "nama" : account.nama,
#                     "username" : account.username,
#                     "email" : account.email,
#                     "password" : account.password
#                 }   
#             )
#             context['form'] = form
#             validate_email_buyer(request)
#     else :
#         form = UpdateProfilBuyer(request.POST, instance= request.user,       
#                 initial = {
#                     # "nama" : account.nama,
#                     "username" : account.username,
#                     "email" : account.email,
#                     "password" : account.password
#                 }   
#             ) 
#         context['form'] = form
#     validate_email_buyer(request)
#     return render(request, 'buyer-profile-edit.html', context)

# def edit_seller(request, *args, **kwargs):
#     if not request.user.is_authenticated:
#         return redirect("login/") 
#     user_id = request.user.id
#     try:
#         account = User.objects.get(pk=user_id)
#     except User.DoesNotExist:
#         return HttpResponse("Something went wrong")
#     context = {}
#     if request.POST:
#         form = UpdateProfilSeller(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('profile_handler/')
#         else :
#             form = UpdateProfilSeller(request.POST, instance= request.user,       
#                 initial = {
#                     "nama" : account.nama,
#                     "username" : account.username,
#                     "email" : account.email,
#                     "password" : account.password,
#                     "namausaha" : account.namausaha,
#                     "deskripsi" : account.deskripsi,
#                     "alamat" : account.alamat,
#                     "kontak" : account.kontak,
#                     "linktoko" : account.linktoko
#                 }   
#             )
#             context['form'] = form
#             validate_email_seller(request)
#     else :
#         form = UpdateProfilSeller(request.POST, instance= request.user,       
#                 initial = {
#                     "nama" : account.nama,
#                     "username" : account.username,
#                     "email" : account.email,
#                     "password" : account.password,
#                     "namausaha" : account.namausaha,
#                     "deskripsi" : account.deskripsi,
#                     "alamat" : account.alamat,
#                     "kontak" : account.kontak,
#                     "linktoko" : account.linktoko
#                 }   
#             ) 
#         context['form'] = form
#     validate_email_seller(request)
#     return render(request, 'seller-profile-edit.html', context)