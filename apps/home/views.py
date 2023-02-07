from django.shortcuts import render
from django.views import View
from apps.cart_shop.models import Product, CartItemShop


class IndexShopView(View):

   def get(self, request):
       data = Product.objects.all()
       cart_items = CartItemShop.objects.filter(cart__user=request.user)
       context = {'data': data,
                  'cart_items': cart_items
                  }
       return render(request, 'home/index.html', context)
