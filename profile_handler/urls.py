from django.urls import path
from .views import *
from django.conf.urls import url

app_name = 'profile'

urlpatterns = [
    path('profile/buyer/', show_buyer, name='show_buyer'),
    path('profile/seller/', show_seller, name='show_seller'),
    # path('edit/buyer/', edit_buyer),
    # path('edit/seller/', edit_seller),
    # url('validate_email/', validate_email, name='validate_email'),
]
