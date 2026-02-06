from django.shortcuts import render

def home(request):
    context = {
        'message': '¡Hola, Django 6!',
    }
    return render(request, 'myapp/home.html', context)
