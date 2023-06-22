from django.urls import path
from .views import Incio, mision, desplegable, formulario, APIrets, index, crear, modificar, eliminar

urlpatterns=[
    path('', Incio , name='Incio'),
    path('mision/', mision, name='mision'),
    path('desplegable/', desplegable, name='desplegable'),
    path('formulario/', formulario, name='formulario'),
    path('APIrets/', APIrets, name='APIrets'),
    path('index/', index ,name='index'),
    path('crear/', crear, name='crear'),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
]