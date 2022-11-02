from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from account.forms import *
from .forms import *

@login_required(login_url='/account/login/')
def show_profile(request):
    if not request.user.is_authenticated:
        return redirect("account/login/")
    if request.user is not None and request.user.is_buyer:
                return redirect('showbuyer/')
    elif request.user is not None and request.user.is_seller:
                return redirect('showseller/')

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