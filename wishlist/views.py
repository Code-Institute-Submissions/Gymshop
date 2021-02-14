from django.shortcuts import render, redirect, reverse, HttpResponse, get_list_or_404, get_object_or_404

from .models import Product, UserProfile, Wishlist, WishlistItem

from django.contrib import messages

# Create your views here.


def wishlist(request):
    """ A view to return the shopping bag """
    items = []
    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist = get_object_or_404(Wishlist, user=profile)
    wishlist_item = get_list_or_404(WishlistItem, wishlist=wishlist)
    for product in wishlist_item:
        products = get_object_or_404(Product, pk=product.id)
        items.append(products)

    context = {
        'wishlist': bool(wishlist),
        'products': items,
    }
    return render(request, 'wishlist/wishlist.html', context)


def add_to_wishlist(request, product_id):


    return render(request, redirect_url)
