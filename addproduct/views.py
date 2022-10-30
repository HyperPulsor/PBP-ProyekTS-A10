from django.shortcuts import render
from .models import *

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json

# @login_required(login_url="/login/")

# def add_product(request):
#     if request.method == 'POST':
#         nama_produk = request.POST.get('nama_produk')
#         kategori_produk = request.POST.get('kategori_produk')
#         harga_produk = request.POST.get('harga_produk')
#         gambar_produk = request.POST.get('gambar_produk')
#         deskripsi_produk = request.POST.get('deskripsi_produk')
#         link_produk = request.POST.get('link_produk')

#         new_project = Project(
#             nama_pemilik=nama_pemilik,
#             nama_project=nama_project,
#             kategori=kategori,
#             bayaran=bayaran,
#             deskripsi=deskripsi,
#             estimasi=estimasi,
#             skills=skills,
#             kontak_pemilik=kontak_pemilik,
#             jumlah_orang=jumlah_orang,
#             id_pemilik=User.objects.get(id=request.user.id),
#             )

#         new_project.save()
        
#         return JsonResponse({"instance": "Proyek Dibuat"}, status=200)
#     return render(request, 'buat_project.html')

# Create your views here.

# def upload(request):
#     if request.method == "POST":
#         images = request.FILES.getlist('images')
#         for image in images:
#             MultipleImage.objects.create(images=image)
#     images = MultipleImage.objects.all()
#     return render(request, 'index.html', {'images': images})