from django.contrib import admin
from .models import CartItemShop, Product, WishlistItemShop

admin.site.register(CartItemShop)
admin.site.register(Product)
admin.site.register(WishlistItemShop)


