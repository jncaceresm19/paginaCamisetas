from django.contrib import admin
from .models import Producto, Marca, Cliente, Pedido, Contacto

class ProductosAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion","stock", "precio", "fecha_recepcion", "marca", "tallas_disponibles"]
    search_fields = ["nombre"]
    list_filter = ["marca", "id"]
    list_per_page = 5
    ordering = ["id"]

# Register your models here.
admin.site.register(Producto, ProductosAdmin)
admin.site.register(Marca)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Contacto)
