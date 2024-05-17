from django.contrib import admin

from goods.models import Categories, Products, Flowers, Composition

admin.site.register(Flowers)
admin.site.register(Composition)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'price']
    list_editable = ['price']
    search_fields = ['name']
    list_filter = ['category']