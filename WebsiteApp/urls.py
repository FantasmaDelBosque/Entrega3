from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('conciertos/', views.conciertos, name="conciertos"),
    path('discos/', views.discos, name="discos"),
    path('shop/', views.shop, name="shop"),
    
    # Formularios
    path('agregar_conciertos/', views.agregar_conciertos, name='agregar_conciertos'),
    path('lista_conciertos/', views.lista_conciertos, name='lista_conciertos'),
    path('agregar_discos/', views.agregar_discos, name='agregar_discos'), 
    path('lista_discos/', views.lista_discos, name='lista_discos'),
    path('agregar_shop/', views.agregar_shop, name='agregar_shop'),
    path('lista_shop/', views.lista_shop, name='lista_shop'),
]
