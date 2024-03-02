from django.shortcuts import render, redirect, HttpResponse
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


def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    return render(request, 'categorias/editar.html', {
        'categoria': categoria
    })


def actualizar_categoria(request, id):
    if request.method == 'POST':
        categoria = Categoria.objects.get(id=id)
        descripcion = request.POST['descripcion']
        categoria.descripcion = descripcion
        categoria.save()
        return redirect('categorias')
    else:
        return redirect('categorias')


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


def eliminar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('categorias')
