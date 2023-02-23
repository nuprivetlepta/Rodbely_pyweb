from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import WishListItemShop, Cart, Product
from apps.cart.models import Cart


class ViewWishlist(View):
    def get(self, request):
        if request.user.is_authenticated:
            wishlist_items = WishListItemShop.objects.filter(wishlist__user=request.user)
            context = {'items': wishlist_items}
            return render(request, 'wishlist/wishlist.html', context)
        else:
            return redirect('auth_shop:login')


class WishListLike(View):
    def get(self, request, product_id):
        if request.user.is_authenticated:
            product = get_object_or_404(Product, id=product_id)
            cart_user = get_object_or_404(Cart, user=request.user)
            wishlist_item = WishListItemShop(wishlist=cart_user, product=product)
            # wishlist_item.save()
            # return redirect('home:index')
            # -------------------------
            for item in WishListItemShop.objects.filter(wishlist__user=request.user):
                if item.product.id == wishlist_item.product.id:
                    return redirect('home:index')
            wishlist_item.save()
            return redirect('home:index')
        else:
            return redirect('auth_shop:login')


class WishListRemove(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart_user = get_object_or_404(Cart, user=request.user)
        # wishlist_item = WishListItemShop(wishlist=cart_user, product=product)
        wishlist_item = get_object_or_404(WishListItemShop, wishlist=cart_user, product=product)
        wishlist_item.delete()
        return redirect('wishlist:wishes')


