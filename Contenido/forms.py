#es una clase que tiene la información que llevará uno o  más formularios en un template
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Plantita, Categoria

class PlantitaForm(forms.ModelForm):
    class Meta:
        model = Plantita 
        fields = ['idProducto','tituloProducto', 'precio', 'descripcion','imagen', 'categoria']
        labels = {
            'idProducto' : "Id",
            'tituloProducto' : "Producto",
            'precio' : "Precio",
            'descripcion' : "Descripcion",
            'imagen' : "Preview",
            'categoria' : "Categoria"
        }
        widgets={
            'patente' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese una id',
                    'class' : 'form-control',
                    'id' : 'idProducto'
                }
            ),
            'marca':forms.TextInput(
                attrs={
                    'placeholder' : 'Producto a vender',
                    'class' : 'form-control',
                    'id' : 'tituloProducto'
                }
            ),
            'modelo':forms.NumberInput(
                attrs={
                    'placeholder' : 'Ingrese el valor',
                    'class' : 'form-control',
                    'id' : 'precio'
                }
            ),
            'marca':forms.TextInput(
                attrs={
                    'placeholder' : 'Descripcion del producto',
                    'class' : 'form-control',
                    'id' : 'descripcion'
                }
            ),
            'imagen':forms.FileInput(
                attrs={
                    'class' : 'form-control',
                    'id' : 'imagen'
                }
            ),
            'categoria':forms.Select(
                attrs={
                    'class' : 'form-control',
                    'id' : 'categoria'
                }
            )
        }