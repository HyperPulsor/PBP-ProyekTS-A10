from django.urls import path
from validasiproduct.views import *

app_name = 'validasi'

urlpatterns = [
    path('', product_invalid, name='product_invalid'),
    path('change_status/<int:id>/', change_status, name='change_status'),
]
