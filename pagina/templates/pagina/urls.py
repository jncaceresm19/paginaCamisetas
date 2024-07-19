from django.urls import path
from .views import index, base, alemania, brasil, argentina, colocolo, cololocal, comprar, madrid, manchester, psg, restodelmundo, selechile, uchile, udechilelocal, contacto, agregar_producto, listar_producto, modificar_producto, eliminar_producto, registro


urlpatterns = [
    path('', index, name='index'),
    path('base/', base, name='base'), 
    path('alemania/', alemania, name='alemania'),
    path('brasil/', brasil, name='brasil'),
    path('argentina/', argentina, name='argentina'),
    path('colocolo/', colocolo, name='colocolo'),
    path('cololocal/', cololocal, name='cololocal'),
    path('comprar/', comprar, name='comprar'),
    path('madrid/', madrid, name='madrid'),
    path('manchester/', manchester, name='manchester'),
    path('psg/', psg, name='psg'),
    path('restodelmundo/', restodelmundo, name='restodelmundo'),
    path('selechile/', selechile, name='selechile'),
    path('uchile/', uchile, name='uchile'),
    path('udechilelocal/', udechilelocal, name='udechilelocal'),
    path('contacto/', contacto, name='contacto'),
    path('registro/', registro, name='registro'),
    path('agregar-producto/', agregar_producto, name='agregar_producto'),   
    path('listar-producto/', listar_producto, name='listar_producto'),
    path('modificar-producto/<id>/', modificar_producto, name='modificar_producto'),


] 
