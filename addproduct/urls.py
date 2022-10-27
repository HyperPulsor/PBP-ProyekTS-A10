from django.urls import path
from . import views

app_name='buat_project'

urlpatterns = [
    path('', views.buat_project, name='buat_project'),
]
