from ast import mod
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta():
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta():
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ("id",)

    def __str__(self):
        return self.name


class Flowers(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    products = models.ManyToManyField(to=Products, through='Composition')

    class Meta():
        db_table = 'flower'
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы'
    
    def __str__(self):
        return self.name


class Composition(models.Model):
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Продукт')
    flower = models.ForeignKey(to=Flowers, on_delete=models.CASCADE, verbose_name='Цветок')
    quantity = models.IntegerField(verbose_name='Количество')

    class Meta():
        db_table = 'composition'
        verbose_name = 'Состав'
        verbose_name_plural = 'Составы'