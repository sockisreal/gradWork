from django.shortcuts import render
from django.template import context

def index(request):
    context = {
        'title': 'FlowerAI - Главная',
        'content': 'Создай свой уникальный букет'
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'FlowerAI - О нас',
        'content': 'О нас',
        'text_on_page': 'Text'
    }
    return render(request, 'main/about.html', context)