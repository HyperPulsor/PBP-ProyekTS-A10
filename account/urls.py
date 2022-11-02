from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('registerbuyer/', views.registerbuyer, name='registerbuyer'),
    path('registerseller/', views.registerseller, name='registerseller'),
    path('adminpage/', views.admin, name='adminpage'),
    path('buyer/', views.buyer, name='buyer'),
    path('seller/', views.seller, name='seller'),
    path('logout/', views.logout_user, name='logout'),
    path('donasi_barang/', views.donasi_barang, name='donasi_barang')
]