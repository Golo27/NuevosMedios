from django.shortcuts import *
from recetas.models import Recet, Comentario
from recetas.forms import RecetaForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def lista_recetas(request):
	recetas = Recet.objects.all()
	return render_to_response('lista_recetas.html',{'lista':recetas},context_instance=RequestContext(request))

def inicio(request):
	return render_to_response('inicio.html')

def nuevo_usuario(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render_to_response('nuevo_usuario.html',{'formulario':formulario}, context_instance=RequestContext(request))

def nueva_receta(request):
    if request.method=='POST':
        formulario = RecetaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/recetas')
    else:
        formulario = RecetaForm()
    return render_to_response('recetaform.html',{'formulario':formulario}, context_instance=RequestContext(request))

def recetas_ABC(request):
    busqueda=Recet.objects.all().order_by('titulo')
    return render_to_response('Alfabeticamente.html',{'busqueda':busqueda}, context_instance=RequestContext(request))

def recetas_order_fecha(request):
    busqueda=Recet.objects.all().order_by('tiempo_registro')
    return render_to_response('by_fecha.html',{'busqueda':busqueda}, context_instance=RequestContext(request))

def eliminar(request):
    

def ingresar(request):
    #if not request.user.is_anonymous():
        #return HttpResponseRedirect('/privado')
    if request.method == 'POST':
    	formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/receta/nueva')
                else:
                    return render_to_response('noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))

       
#@login_required(login_url='/ingresar')
def privado(request):
    usuario = request.user
    return render_to_response('privado.html', {'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')