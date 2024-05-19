from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

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

def gen_photo(request):
    context = {
        'title': 'FlowerAI - Букет от ИИ'
    }
    return render(request, 'main/gen.html', context)

def generate_image(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data.get('prompt')

        # Отправка запроса на ваш сервис
        response = requests.post('http://stabgen.desolator.net/generate', json={'prompt': prompt})
        response_data = response.json()
        image_data = response_data.get('image_data')

        return JsonResponse({'image_data': image_data})

    return JsonResponse({'error': 'Invalid request'}, status=400)
