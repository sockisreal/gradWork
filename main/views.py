from django.shortcuts import render
from django.template import context

def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница'
    }
    return render(request, 'main/index.html', context)
