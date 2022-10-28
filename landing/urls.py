from django.urls import path
from landing.views import *

app_name = 'landing'

urlpatterns = [
    path('', add_item_seller, name='add_item_seller'),
    path('show_item/', show_item, name='show_item'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('json/', show_json, name='show_json'),
    path('show/', show_function, name='show_function')
]