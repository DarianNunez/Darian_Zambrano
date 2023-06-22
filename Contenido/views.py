from django.shortcuts import render, redirect
from .models import Plantita, Categoria
from .forms import PlantitaForm
# Create your views here.

def Incio(request):
    return render(request,'Incio.html')
     
def formulario(request):
    return render(request,'formulario.html')

def APIrets(request):
    return render(request,'APIrets.html')

def desplegable(request):
    return render(request,'desplegable.html')

def mision(request):
    return render(request,'mision.html')

def index(request):
    plantitas= Plantita.objects.all()
    datos={'plantitas' : plantitas}
    return render(request, 'index.html', datos)

def crear(request):
    if request.method=="POST":
        plantitaform = PlantitaForm(request.POST)
        if plantitaform.is_valid():
            plantitaform.save() #similar en funcion al metodo insert
            return redirect ('index')
    else:
        plantitaform=PlantitaForm()
    return render(request, 'crear.html', {'plantitaform' : plantitaform})

def eliminar(request, id):
    plantitaEliminada=Plantita.objects.get(idProducto=id)
    plantitaEliminada.delete()
    return redirect('index')


def modificar(request,id):
    plantitaModificada = Plantita.objects.get(idProducto=id)
    datos ={
        'form': PlantitaForm(instance=plantitaModificada)   #el objeto form llega al template
    }
    if request.method=="POST":          #modificamos backend con los cambios realizados
        formulario = PlantitaForm(data=request.POST, instance=plantitaModificada)
        if formulario.is_valid():
            formulario.save()           #modificamos el objeto
            return redirect('index')
    return render(request,'modificar.html', datos)
