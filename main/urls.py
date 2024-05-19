from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('generate-photo/', views.gen_photo, name='gen_photo'),
    path('generate-image/', views.generate_image, name='generate_image'),  # Добавьте эту строку
]
