from django.urls import path
from . import views

<<<<<<< HEAD
urlpatterns = [
    path('index/', views.index, name= 'index'),
=======
app_name = 'account'

urlpatterns = [
    path('', views.index, name= 'index'),
>>>>>>> 3141d3d85fd05be510a87837a2e96bda38670caf
    path('login/', views.login_view, name='login_view'),
    path('registerbuyer/', views.registerbuyer, name='registerbuyer'),
    path('registerseller/', views.registerseller, name='registerseller'),
    path('adminpage/', views.admin, name='adminpage'),
    path('buyer/', views.buyer, name='buyer'),
    path('seller/', views.seller, name='seller'),
<<<<<<< HEAD
=======
    path('logout/', views.logout_user, name='logout'),
    path('donasi_barang/', views.donasi_barang, name='donasi_barang')
>>>>>>> 3141d3d85fd05be510a87837a2e96bda38670caf
]