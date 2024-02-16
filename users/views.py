from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.


def sign_up(request):
    return render(request, 'register.html')


def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = User.objects.create_user(
            username=username, password=password)
        usuario.save()
        return redirect('sign')
    else:
        return redirect('sign')


def login(request):
    pass
