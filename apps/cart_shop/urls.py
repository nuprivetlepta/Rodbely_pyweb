from django.urls import path
from .views import ViewCart, ViewCartBuy, ViewCartAdd, ViewCartDel

app_name = 'cart_shop'

urlpatterns = [
   path('', ViewCart.as_view(), name='cart'),
   path('buy/<int:product_id>', ViewCartBuy.as_view(), name='buy'),
   path('add/<int:product_id>', ViewCartAdd.as_view(), name='add_to_cart'),
   path('del/<int:item_id>', ViewCartDel.as_view(), name='del_from_cart'),
]
