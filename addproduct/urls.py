
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name='addproduct'

urlpatterns = [
    path('json/ajax/', views.create_product, name='create_product'),
    path('json/', views.show_json, name="show_json"),
    path('katalog/add/', views.show_product, name='show_product'), 
    path('details/',views.product_details, name='product_details'),
    path('show_details/<int:id>/',views.show_details, name='show_details'),
   
]

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
