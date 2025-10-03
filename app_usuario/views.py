from django.shortcuts import render

def index(request):
    usuarios = [
        {'nombre': 'Alice', 'edad': 30, 'ciudad': 'Nueva York'},
        {'nombre': 'Bob', 'edad': 24, 'ciudad': 'Los Ángeles'},
        {'nombre': 'Charlie', 'edad': 35, 'ciudad': 'Chicago'},
    ]
    return render(request, 'index.html', {'usuarios':usuarios})