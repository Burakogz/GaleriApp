from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.


def index(request):
    return render(request, "galeri/index.html")
def albumler(request):
    return render(request, "galeri/albumler.html")
def notlar(request):
    return render(request, "galeri/notlar.html")

def bbk(request):
    return render(request, "galeri/bbk.html")
def piknik(request):
    return render(request, "galeri/piknik.html")
def istanbul(request):
    return render(request, "galeri/istanbul.html")
def anilar(request):
    return render(request, "galeri/anilar.html")

def blog_details(request,id):
    return render(request, "galeri/blog_details.html",{
        "id":id
    })
    