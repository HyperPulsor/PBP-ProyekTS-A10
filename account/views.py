from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime

from .forms import *

# Create your views here.

def main(request):
    if (request.user.is_authenticated):
        return render(request, "main.html")
    else:
        return HttpResponseRedirect(reverse('account:login'))

def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('account:main'))
    return render(request, "signup.html")

def buyer_signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('account:main'))
    
    if request.method == "POST":
        print(request.POST)
        form = BuyerSignupForm(request.POST)

        username_exists = User.objects.filter(username=request.POST.get("username")).exists()
        email_exists = User.objects.filter(email=request.POST.get("email")).exists()

        data = {}

        if '@' in request.POST.get("username"):
            data['success'] = False
            data['warning'] = "Username can not contain @."
    
        elif username_exists:
            data['success'] = False
            data['warning'] = "Username has already been used."

        elif email_exists:
            data['success'] = False
            data['warning'] = "Email has already been used."

        else:
            if form.is_valid():
                data['success'] = True
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.is_buyer = True
                user.is_seller = False
                user.is_superadmin = False
                user.is_adminr = False
                user.is_staff = False
                user.save()

            else:
                data['error'] = form.errors
                data['success'] = False
                context = {"form": form}

        response = HttpResponse(json.dumps(data), content_type='application/json', status=200)
        return response        

    form = BuyerSignupForm()
    context = {"form": form}

    return render(request, 'signup.html', context)

def seller_signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('account:main'))
    
    if request.method == "POST" and is_ajax:
        form = SellerSignupForm(request.POST)
        name_exists = User.objects.filter(is_seller=True, name=request.POST.get("name")).exists()
        email_exists = User.objects.filter(email=request.POST.get("email")).exists()
        data = {}
    
        if name_exists:
            data['success'] = False
            data['warning'] = "Institute name has already been registered."
            
        elif email_exists:
            data['success'] = False
            data['warning'] =  "Email has already been used."
            
        else:
            if form.is_valid():
                data['success'] = True
                user = form.save(commit=False)
                user.is_seller = True
                user.is_buyer = False
                user.is_superadmin = False
                user.is_adminr = False
                user.is_staff = False
                user.save()
                
            else:
                data['error'] = form.errors
                data['success'] = False
                context = {"form": form}
                
        response = HttpResponse(json.dumps(data), content_type='application/json', status=200)
        return response

    form = SellerSignupForm()
    context = {"form": form}

    return render(request, "signup.html", context)

def login_user(request):
    # Excecuted when User submit the form.
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('account:main'))

    if request.method == 'POST':
        # Authenticate User based on username and password.
        user_input = request.POST['email']

        try:
            email = User.objects.get(username=user_input).email
        except User.DoesNotExist:
            email = request.POST['email']

        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        # Executed when User is valid. Redirect to home page.
        if user is not None:
            login(request, user)
            response = redirect('account:main')
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response

        # Executed when User is not valid. Redirect to login page.
        else:
            messages.success(request, 'Invalid login. Please try again!')

    # Rendering login.html.
    return render(request, "login.html")

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('account:login'))
    response.delete_cookie('last_login')
    request.session.flush()
    return response

def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'