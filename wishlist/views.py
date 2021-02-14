from django.shortcuts import render, redirect, reverse, HttpResponse, get_list_or_404, get_object_or_404

from .models import Product, UserProfile, Wishlist, WishlistItem

from django.contrib import messages

# Create your views here.


def wishlist(request):
    """ A view to return the shopping bag """
    profile = get_object_or_404(UserProfile, user=request.user)
    print(profile)
    wishlist = get_object_or_404(Wishlist, user=profile)
    print(wishlist)
    wishlist_item = get_list_or_404(WishlistItem, wishlist=wishlist)
    print(wishlist_item)
    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, product_id):


    return render(request, redirect_url)
