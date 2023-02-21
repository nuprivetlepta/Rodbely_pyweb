from django.urls import path
from .views import ViewWishlist

app_name = 'wishlist'

urlpatterns = [
   path('', ViewWishlist.as_view(), name='wishes'),
]
