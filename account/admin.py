from django.contrib import admin

from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *

# Register your models here.

class CustomUserAdmin(UserAdmin):
    
    list_display = ('name', 'email','username','is_admin','is_staff', 'is_buyer', 'is_seller', 'deskripsi')
    search_fields = ('email','username')

    add_fieldsets = (
        (None, {
            'fields': ('name', 'email', 'password1', 'password2', 'is_superuser', 'is_staff', 'is_admin')}
        ),
    )
    
admin.site.register(User, CustomUserAdmin) 




##BATAAS SUCI##
# admin.site.register(User)