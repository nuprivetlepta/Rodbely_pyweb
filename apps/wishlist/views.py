from django.shortcuts import render
from django.views import View


class ViewWishlist(View):
    def get(self, request):
        return render(request, 'wishlist/wishlist.html')