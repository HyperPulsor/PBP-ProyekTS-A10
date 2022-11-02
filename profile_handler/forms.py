# from django import forms
from django import forms as auth_forms
# from account.forms import SignUpBuyerForm, SignUpSellerForm
from account.models import User
from django.contrib.auth.forms import UserChangeForm, ReadOnlyPasswordHashField

class BuyerEditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        

class SellerEditProfileForm(UserChangeForm):
    class Meta:
        model = User
        # fields = ['name','username','email','password', 'namausaha', 'kategori', 'deskripsi', 'address', 'kontak', 'linktoko']
        fields = ['username', 'email',]