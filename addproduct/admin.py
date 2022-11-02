from django.contrib import admin
<<<<<<< HEAD
from django.db import models

from addproduct.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Product, ProductAdmin)
=======
from addproduct.models import Product

# Register your models here.
admin.site.register(Product)
>>>>>>> 3141d3d85fd05be510a87837a2e96bda38670caf
