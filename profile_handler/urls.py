from django.urls import path
from .views import *
# from django.conf.urls import url
from django.contrib.auth import views as auth_views
# from . import views

app_name = 'profile'

urlpatterns = [
    path('', show_profile, name='profile'),
    path('showbuyer/', show_buyer, name='showbuyer'),
    path('showseller/', show_seller, name='showseller'),
    path('edit/buyer/', BuyerEditView.as_view(), name='editbuyer'),
    path('edit/seller/', SellerEditView.as_view(), name='editseller'),
    path('edit/password/', PasswordsChangeView.as_view(template_name='change-password.html')),
    path('password_success', password_success, name='password_success'),
]
