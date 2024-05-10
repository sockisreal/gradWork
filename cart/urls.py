from django.urls import path

from cart import views

app_name = 'cart'

urlpatterns = [
    path('cart-add/<slug:product_slug>/', views.cart_add, name='cart-add'),
    path('cart-change/<slug:product_slug>/', views.cart_change, name='cart-change'),
    path('cart-remove/<slug:product_slug>/', views.cart_remove, name='cart-remove'),
]
