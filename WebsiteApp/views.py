from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Conciertos, Discos, Shop
from .forms import ConciertosForm, DiscosForm, ShopForm


def inicio(request):
    return render(request, "inicio.html")

def conciertos(request):
    return render(request, 'conciertos.html')

def discos(request): 
    return render(request, "discos.html")

def shop(request):
    return render(request, "shop.html")

def lista_conciertos(request):
    conciertos = Conciertos.objects.all() # pylint: disable=no-member
    return render(request, 'lista_conciertos.html', {'conciertos': conciertos})

def lista_discos(request):
    discos = Discos.objects.all() # pylint: disable=no-member
    return render(request, 'lista_discos.html', {'discos': discos})

def lista_shop(request):
    shops = Shop.objects.all() # pylint: disable=no-member
    return render(request, 'lista_shop.html', {'shops': shops})


def agregar_conciertos(request):
    if request.method == 'POST':
        form = ConciertosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_conciertos')
    else:
        form = ConciertosForm()
    
    return render(request, 'agregar_conciertos.html', {'form': form})

def agregar_discos(request):
    if request.method == 'POST':
        form = DiscosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_discos')
    else:
        form = DiscosForm()
    
    return render(request, 'agregar_discos.html', {'form': form})



def agregar_shop(request):
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_shop')
    else:
        form = ShopForm()
    
    return render(request, 'agregar_shop.html', {'form': form})

