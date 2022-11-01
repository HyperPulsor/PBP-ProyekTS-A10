from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from addkategori.models import Kategori

@login_required(login_url='/index/')
def show_landing(request):
    kategori_item = Kategori.objects.all()
    context = {
        'kategori_item' : kategori_item,
    }
    return render(request, "show.html", context)