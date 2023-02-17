from .models import CartItemShop
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .models import CartItemShop, Cart, Product
from decimal import Decimal

def save_product_in_cart(request, product_id):
   cart_items = CartItemShop.objects.filter(cart__user=request.user,
                                            product__id=product_id)
   if cart_items:
       cart_item = cart_items[0]
       cart_item.quantity += 1
   else:
       product = get_object_or_404(Product, id=product_id)
       cart_user = get_object_or_404(Cart, user=request.user)
       cart_item = CartItemShop(cart=cart_user, product=product)
   cart_item.save()


class ViewCart(View):
   def get(self, request):
       cart_items = CartItemShop.objects.filter(cart__user=request.user)
       data = list(cart_items)
       total_price_no_discount = sum(item.product.price * item.quantity
                                     for item in data)
       total_discount = sum(item.product.price * item.product.discount * item.quantity
                            for item in data if item.product.discount is not None)/100
       if total_price_no_discount == 0:
           total_price_no_discount = Decimal("0.00")
       if total_discount == 0:
           total_discount = Decimal("0.00")
       total_sum = total_price_no_discount - total_discount
       context = {'cart_items': data,
                  'total_price_no_discount': total_price_no_discount,
                  'total_discount': total_discount,
                  'total_sum': total_sum,
                  }
       return render(request, 'cart_shop/cart.html', context)


class ViewCartBuy(View):
   def get(self, request, product_id):
       save_product_in_cart(request, product_id)
       return redirect('cart_shop:cart')

class ViewCartAdd(View):
   def get(self, request, product_id):
       save_product_in_cart(request, product_id)
       return redirect('home:index')

class ViewCartDel(View):
   def get(self, request, item_id):
       cart_item = get_object_or_404(CartItemShop, id=item_id)
       cart_item.delete()
       return redirect('cart_shop:cart')



