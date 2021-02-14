from django.shortcuts import render, redirect, reverse, HttpResponse, get_list_or_404, get_object_or_404

from .models import Product, UserProfile, Wishlist

from django.contrib import messages

# Create your views here.


def wishlist(request):
    """ A view to return the shopping bag """
    wishlist = get_list_or_404(Wishlist, user=request.user)
    wishlist_items = {}
    for items in wishlist.wished_item:
        wishlist_items.append(items)
    context = {
        'wishlist': wishlist_items
    }
    return render(request, 'wishlist/wishlist.html', context)


def add_to_wishlist(request, product_id):
    

    return render(request, redirect_url)
