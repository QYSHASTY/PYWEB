from django.contrib import admin
from .models import Cart, CartItem, Product, Wishlist

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Product)
admin.site.register(Wishlist)


