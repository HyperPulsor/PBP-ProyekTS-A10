from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('registerbuyer/', views.registerbuyer, name='registerbuyer'),
    path('registerseller/', views.registerseller, name='registerseller'),
    path('adminpage/', views.admin, name='adminpage'),
    path('buyer/', views.buyer, name='buyer'),
    path('seller/', views.seller, name='seller'),
]