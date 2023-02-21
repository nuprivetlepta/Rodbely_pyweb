from django.urls import path
from .views import ViewWishlist

app_name = 'cart_shop'

urlpatterns = [
   path('', ViewWishlist.as_view(), name='wishlist'),
]
