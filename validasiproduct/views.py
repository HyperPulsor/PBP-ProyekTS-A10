from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect
from addproduct.views import Product
from addproduct.models import Product

def product_invalid(request):
    data = Product.objects.all()
    context = {
    'list_product': data,
}
    return render(request, "validasi.html", context) 

def change_status(request, id):
    data = Product.objects.get(pk=id)
    data.is_valid = not(data.is_valid)
    data.save()
    return redirect('validasi:product_invalid')