from django.urls import path
from .views import ViewWishlist, WishListLike, WishListRemove

app_name = 'wishlist'

urlpatterns = [
   path('', ViewWishlist.as_view(), name='wishes'),
   path('like/<int:product_id>', WishListLike.as_view(), name='like'),
   path('remove/<int:product_id>', WishListRemove.as_view(), name='remove')
]
