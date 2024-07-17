from django.urls import path
from .views import index, base, colocolo, cololocal, comprar, restodelmundo, selechile, uchile, udechilelocal, contacto, agregar_producto, listar_producto, modificar_producto, eliminar_producto, registro, detalleP


urlpatterns = [
    path('', index, name='index'),
    path('base/', base, name='base'), 
    path('colocolo/', colocolo, name='colocolo'),
    path('cololocal/<int:producto_id>/', cololocal, name='cololocal'),
    path('comprar/', comprar, name='comprar'),
    path('restodelmundo/', restodelmundo, name='restodelmundo'),
    path('selechile/', selechile, name='selechile'),
    path('uchile/', uchile, name='uchile'),
    path('udechilelocal/', udechilelocal, name='udechilelocal'),
    path('contacto/', contacto, name='contacto'),
    path('registro/', registro, name='registro'),
    path('agregar-producto/', agregar_producto, name='agregar_producto'),   
    path('listar-producto/', listar_producto, name='listar_producto'),
    path('modificar-producto/<id>/', modificar_producto, name='modificar_producto'),
    path('detalleP/<int:producto_id>/', detalleP, name='detalleP'),
] 
