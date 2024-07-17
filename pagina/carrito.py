class Carrito:
    def __init__(self, request):
        self.request = request
        self.carrito = self.request.session.get('carrito', {})

    def agregar(self, producto, nombre=None, numero=None, talla=None):
        id = str(producto.id)
        precio_extra = 0

        if nombre:
            precio_extra += 5000
        if numero:
            precio_extra += 5000

        if id not in self.carrito:
            self.carrito[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio + precio_extra,
                "cantidad": 1,
                "acumulado": producto.precio + precio_extra,
                "imagen": producto.imagen.url if producto.imagen else None,
                "talla": talla if talla else None,  
                "personalizacion": {
                    "nombre": nombre,
                    "numero": numero,
                }
            }
        else:
            self.carrito[id]["cantidad"] += 1
            if 'acumulado' not in self.carrito[id]:
                self.carrito[id]['acumulado'] = 0
            self.carrito[id]['acumulado'] += producto.precio + precio_extra


        if producto.stock > 0:
            producto.stock -= 1
            producto.save()
        else:
            raise ValueError("Sin Stock.")

        self.guardar()

    def guardar(self):
        self.request.session['carrito'] = self.carrito
        self.request.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio

            producto.stock += 1
            producto.save()

            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(producto)
            self.guardar()
    
    def sumar(self, producto):
       id = str(producto.id)
       if id in self.carrito.keys():
          self.carrito[id]["cantidad"] += 1
          self.carrito[id]["acumulado"] += producto.precio

          producto.stock -= 1
          producto.save()

          self.guardar()
          
    def limpiar(self):
        self.request.session["carrito"] = {}
        self.request.session.modified = True


