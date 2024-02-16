from django.shortcuts import render, redirect
from . models import Categoria
from django.contrib.auth.models import User
# Create your views here.


def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/categorias.html', {
        'categorias': categorias
    })


def nueva_categoria(request):
    return render(request, 'categorias/nueva_categoria.html')


def guardar_categoria(request):
    if request.method == 'POST':
        descripcion = request.POST['descripcion']
        estado = bool(request.POST.get('estado'))
        if estado == 'on':
            estado = True
        elif estado == 'off':
            estado = False

        nueva_categoria = Categoria(
            descripcion=descripcion,
            estado=estado
        )
        nueva_categoria.save()
        return redirect('categorias')

    else:
        return redirect('categorias')
