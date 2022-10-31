from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/index/')
def show_landing(request):
    return render(request, "show.html")