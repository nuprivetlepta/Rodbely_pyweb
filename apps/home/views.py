from django.shortcuts import render
from django.views import View
from apps.cart_shop.models import Product


class IndexShopView(View):

   def get(self, request):
       data = Product.objects.all()
       context = {'data': data
                  }
       return render(request, 'home/index.html', context)
