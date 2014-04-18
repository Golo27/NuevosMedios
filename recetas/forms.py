#encoding:utf-8 
from django.forms import ModelForm
from django import forms
from recetas.models import Recet, Comentario

class RecetaForm(ModelForm):
    class Meta:
        model = Recet