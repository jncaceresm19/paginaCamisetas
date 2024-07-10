from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Talla(models.Model):
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    stock = models.IntegerField()
    precio = models.IntegerField()
    fecha_recepcion = models.DateField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)  
    talla = models.ManyToManyField(Talla) 
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    direccion = models.TextField()
    
    def __str__(self):
        return self.nombre

opciones_consultas = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    fecha_pedido = models.DateField()
    
    def __str__(self):
        return f"Pedido {self.id} de {self.cliente.nombre}"

