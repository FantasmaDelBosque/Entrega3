from django import forms
from .models import Conciertos, Discos, Shop



# Formulario eventos

class ConciertosForm(forms.ModelForm):
    class Meta:
        model = Conciertos
        fields = ['fecha', 'lugar', 'pais', 'estado', 'boton_compra']
               
class DiscosForm(forms.ModelForm):
    class Meta:
        model = Discos
        fields = ['titulo', 'anio_lanzamiento', 'portada', 'url_compra']   

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'categoria', 'disponible']
