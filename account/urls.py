from django.urls import path
from account.views import *

app_name = 'account'
urlpatterns = [
    path('', main, name='main'),
    path('signup/', signup, name='signup'),
    path('signup/buyer/', buyer_signup, name='buyer_signup'),
    path('signup/seller/', seller_signup, name='seller_signup'),
     path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]