from django.shortcuts import render
# import models
from adminfaq.models import *
# import form
from .forms import FormFaq
# import dll
from django.shortcuts import redirect
from django.http.response import JsonResponse, HttpResponse
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def show_faq(request):
    form = FormFaq()
    data = Faq.objects.all()
    context = {
        'title' : 'Frequently Asked Question',
        'faq' : data,
        'form' : form,
        }
    return render(request, "home.html", context)

@csrf_exempt
def create_faq(request):
    if request.method == "POST":
        form = FormFaq(request.POST)
        if form.is_valid():
            form = Faq()
            form.user = request.user
            form.question = request.POST.get('question')
            form.answer = request.POST.get('answer')
            form.save()
            return redirect('faq:show_faq')
    else:
        form = FormFaq()
    # context = {'form': form}
    # return render(request, 'faq.html', context)
    return JsonResponse({"instance": "FAQ Ditambahkan"},status=200)
    
def show_json(request):
    data = Faq.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def delete_faq(request, id):
    deletefaq = Faq.objects.get(pk=id)
    deletefaq.delete()
    # return redirect('faq:show_faq')
    return JsonResponse({'error': False})

