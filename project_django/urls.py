"""project_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('addproduct/', include('addproduct.urls')),
    path('account/', include('account.urls')),
    path('katalog/', include('katalog.urls')),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('adminfaq/', include('adminfaq.urls')),
    path('addproduct', include('addproduct.urls')),
    path('validasiproduct/', include('validasiproduct.urls')),
    path('addkategori/', include('addkategori.urls')),
    path('', include('account.urls')),
    path('forum/', include('forum.urls')),
    path('katalog/', include('katalog.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 3141d3d85fd05be510a87837a2e96bda38670caf
