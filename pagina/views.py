from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm, ProductoForm, LoginForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required



# Create your views here.

def index(request):
    restodelmundo_ids = [1, 3, 6, 7, 11, 5]
    productos_internacionales = Producto.objects.filter(pk__in=restodelmundo_ids)

    chile_ids = [15, 16, 18]
    productos_chile = Producto.objects.filter(pk__in=chile_ids)

    data = {
        'productos_internacionales': productos_internacionales,
        'productos_chile': productos_chile,
    }
    return render(request, 'pagina/index.html', data)

def alemania(request):
    return render(request, 'pagina/alemania.html')

def brasil(request):
    return render(request, 'pagina/brasil.html')

def argentina(request):
    return render(request, 'pagina/argentina.html')

def colocolo(request):
    colocolo_ids = [15, 16, 17]
    productos_colo = Producto.objects.filter(pk__in=colocolo_ids)

    interes_ids = [3, 8, 12]
    productos_interes = Producto.objects.filter(pk__in=interes_ids)

    data = {
        'productos_colo': productos_colo,
        'productos_interes': productos_interes,
    }
    return render(request, 'pagina/colocolo.html', data)

def cololocal(request):
    return render(request, 'pagina/cololocal.html')

def comprar(request):
    return render(request, 'pagina/comprar.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Enviado"
        else: 
            data["form"] = formulario


    return render(request, 'pagina/contacto.html', data)

def madrid(request):
    return render(request, 'pagina/madrid.html')

def manchester(request):
    return render(request, 'pagina/manchester.html')

def psg(request):
    return render(request, 'pagina/psg.html')


def restodelmundo(request):
    resto_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    productos_restomundo = Producto.objects.filter(pk__in=resto_ids)

    interes_ids = [15, 16, 18]
    productos_interes = Producto.objects.filter(pk__in=interes_ids)

    data = {
        'productos_restomundo': productos_restomundo,
        'productos_interes': productos_interes,
    }
    return render(request, 'pagina/restodelmundo.html', data)


def selechile(request):
    return render(request, 'pagina/selechile.html')

def uchile(request):
    lau_ids = [18, 19, 20]
    productos_u = Producto.objects.filter(pk__in=lau_ids)

    interes_ids = [2, 7, 11]
    productos_interes = Producto.objects.filter(pk__in=interes_ids)

    data = {
        'productos_u': productos_u,
        'productos_interes': productos_interes,
    }
    return render(request, 'pagina/uchile.html', data)

def udechilelocal(request):
    return render(request, 'pagina/udechilelocal.html')

@permission_required('pagina.add_producto')
def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado correctamente")
        else:
            data["form"] = formulario

    return render(request, 'producto/agregar.html', data)

@permission_required('pagina.view_producto')
def listar_producto(request):
    producto = Producto.objects.all()

    data = {
        'producto': producto
    }
    return render(request, 'producto/listar.html', data)

@permission_required('pagina.change_producto')
def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to= "listar_producto")
        else:
            data["form"] = formulario

    return render(request, 'producto/modificar.html', data)

@permission_required('pagina.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to='listar_producto')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                error_message = "Nombre de usuario o contraseña incorrectos."
                return render(request, 'registration/login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def registro(request):
    data={
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="index")
        data["form"]=formulario
    return render(request, 'registration/registro.html', data)

