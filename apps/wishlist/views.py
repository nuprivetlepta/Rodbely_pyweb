from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import WishListItemShop, Cart, Product
from apps.cart.models import Cart


class ViewWishlist(View):
    # def get(self, request):
    #     return render(request, 'wishlist/wishlist.html')

    def get(self, request):
        wishlist_items = WishListItemShop.objects.filter(wishlist__user=request.user)
        context = {'items': wishlist_items}
        return render(request, 'wishlist/wishlist.html', context)

class WishListLike(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart_user = get_object_or_404(Cart, user=request.user)
        wishlist_item = WishListItemShop(cart=cart_user, product=product)
        wishlist_item.save()
        return redirect('home:index')

