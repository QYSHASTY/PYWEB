from django.urls import path
from .views import ViewCart, ViewWishlist, ViewCartAdd, ViewWishAdd

app_name = 'cart_shop'


urlpatterns = [
   path('cart/', ViewCart.as_view(), name='cart'),
   path('cart_add/<int:product_id>', ViewCartAdd.as_view(), name='add_to_cart'),
   path('wishlist/', ViewWishlist.as_view(), name='wishlist'),
   path('wishlist_add/<int:product_id>', ViewWishAdd.as_view(), name='wishlist_add'),
]




