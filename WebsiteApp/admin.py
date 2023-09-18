from django.contrib import admin
from .models import Conciertos, Discos, Shop

# Register your models here.

admin.site.register(Conciertos)

admin.site.register(Discos)

admin.site.register(Shop)