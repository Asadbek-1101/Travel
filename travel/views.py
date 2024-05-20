from django.shortcuts import render, redirect, get_object_or_404
from .models import Categories, Davlatlar, Reys, Country
from .forms import CreateDavlat

#-------------------------------------------------------------------------------------------------
# Tartiblovchi funksiyalar

def home(request):
    catigories = Categories.objects.all()
    davlat = Davlatlar.objects.all()

    return render(request, 'home.html', {"davlat":davlat, "cat":catigories})

def destination(request, id):
    catigories = get_object_or_404(Categories, id=id)
    davlat = catigories.davlat.all()

    return render(request, 'destination.html', {"davlat":davlat, "cat":catigories})

#-------------------------------------------------------------------------------------------------
# CRUD

def batafsil(request, id):
    davlat = get_object_or_404(Davlatlar, id=id)
    return render(request, 'batafsil.html', {"davlat":davlat})

def batafsil2(request, id):
    country = get_object_or_404(Country, id=id)
    return render(request, 'batafsil2.html', {"country":country})

def create_davlat(request):
    form = CreateDavlat()
    if request.method == "POST":
        form = CreateDavlat(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'create_davlat.html', {"form":form})

def update_davlat(request, id):
    davlat = get_object_or_404(Davlatlar, id=id)
    form = CreateDavlat(instance=davlat)
    if request.method == "POST":
        form = CreateDavlat(request.POST, instance=davlat)
        if form.is_valid():
            form.save()
            return redirect('batafsil', id=davlat.id)
    return render(request, 'create_davlat.html', {"form": form})

def delete_davlat(request, id):
    davlat = get_object_or_404(Davlatlar, id=id)
    davlat.delete()
    return redirect('/')
#-------------------------------------------------------------------------------------------------
# Pagelarni tartiblash va ulash

def reyslar(request):
    reyslar = Reys.objects.all()
    country = Country.objects.all()
    return render(request, 'reyslar.html', {"reyslar":reyslar, "country":country})


def country(request, id):
    reyslar = get_object_or_404(Reys, id=id)
    country = reyslar.country.all()
    return render(request, 'country.html', {"reyslar":reyslar, "country":country})

def xizmatlar(request):
    catigories = Categories.objects.all()
    davlat = Davlatlar.objects.all()
    return render(request, 'xizmatlar.html', {"davlat": davlat, "cat": catigories})

#-------------------------------------------------------------------------------------------------
# Hech qanday jo'natma talab qilmaydigan page

def about(request):
    return render(request, 'about.html')

