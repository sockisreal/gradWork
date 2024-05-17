from django.shortcuts import render
from django.template import context

from goods.models import Categories

def index(request):
    context = {
        'title': 'FlowerAI - Главная',
        'content': 'Создай свой уникальный букет',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'FlowerAI - О нас',
        'content': 'О нас'
    }
    return render(request, 'main/about.html', context)