from audioop import reverse
from pyexpat.errors import messages
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from requests import request

from addproduct.forms import *
from .models import *
from .forms import *

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json



def show_json(request):
    data = Product.objects.filter(is_valid=True)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# def show_product(request):
#     product_list = Product.objects.filter(user=request.user)
#     context = {
#         'products' : product_list,
#     }
#     return render(request, "catalog.html", context)

# @login_required(login_url='login/')
def show_product(request):
    form = AddProductForm() 
    product = Product.objects.filter(is_valid=True)
    context = {
    'product': product,
    'form': form
    }
    if product is not None:
        return render(request, "catalog.html",context=context)
    else:
        raise Http404('Produk tidak ada')


# @login_required(login_url='login/')
def create_product(request):
    print(request.method)
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        print('masuk')
        print(form.is_valid())
    
        if form.is_valid:
            form.instance.user = request.user
            form.instance.is_valid = False
            form.save()
            return JsonResponse({'status':200}) 


def show_details(request, id):
    product = Product.objects.get(pk=id)
    context = {
    'product': product,
    }
    if product is not None:
        return render(request, "product_details.html",context=context)
    else:
        raise Http404('Produk tidak ada')
            

def product_details(request):
    return HttpResponseRedirect(reverse("addproduct:show_details"))

def delete_product(request, id):
    product = Product.objects.get( pk = id)
    product.delete()
    return redirect('addproduct:show_product')








