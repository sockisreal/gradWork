from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from goods.models import Composition, Products, Categories
from goods.utils import q_search
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
import base64
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt

@login_required
def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 9)
    current_page = paginator.page(int(page))

    context = {
        'title': 'FlowerAI - Каталог',
        'goods': current_page,
        'slug_url': category_slug
    }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    composition = Composition.objects.filter(product__slug=product_slug)
    context = {
        'title': 'FlowerAI - Товар',
        'product': product,
        'composition': composition
    }
    return render(request, 'goods/product.html', context=context)


def add_product(request):
    print("1=======================")
    print(request)
    print("1=======================")
    if request.method == 'POST':
        print("2=======================")
        print(request)
        print("2=======================")
        try:
            data = json.loads(request.body)

            # Получение данных из POST-запроса
            name = data.get('name')
            price = data.get('price')
            image_data = data.get('image_data')
            category = Categories.objects.first()  # Пример, выбираем первую категорию

            if not name or not price or not image_data:
                return JsonResponse({'success': False, 'error': 'Missing required fields'})

            # Создание slug из имени продукта
            slug = slugify(name + '-' + str(datetime.datetime.now().timestamp()))

            # Декодирование изображения из base64
            format, imgstr = image_data.split(';base64,')
            ext = format.split('/')[-1]
            image = ContentFile(base64.b64decode(imgstr), name=f'{slug}.{ext}')

            # Создание нового продукта
            product = Products.objects.create(
                name=name,
                slug=slug,
                image=image,
                price=price,
                category=category
            )

            return JsonResponse({'success': True, 'product_id': product.id})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
