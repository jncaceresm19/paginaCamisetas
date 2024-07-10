from django.contrib import admin
from .models import Producto, Marca, Cliente, Pedido, Contacto, Talla


class ProductosAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion", "stock", "precio", "fecha_recepcion", "marca", "tallas_disponibles"]
    search_fields = ["nombre"]
    list_filter = ["marca", "id"]
    list_per_page = 5
    ordering = ["id"]

    def tallas_disponibles(self, obj):
        return ", ".join([talla.nombre for talla in obj.talla.all()])

    tallas_disponibles.short_description = 'Tallas Disponibles'

# Register your models here.
admin.site.register(Producto, ProductosAdmin)
admin.site.register(Marca)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Contacto)
admin.site.register(Talla)
