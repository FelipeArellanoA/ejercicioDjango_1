from django.shortcuts import render

# Create your views here.

from .services import libros

def base(request):
    return render(request, 'base.html', {})

def index(request):
    return render(request, 'index.html', {})

def lista_libros(request):
    context= {
        'libros': libros
    }
    return render(request, 'lista_libros.html', context)

