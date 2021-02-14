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
    profile = get_object_or_404(UserProfile, user=request.user)
    print(profile)
    wishlist = get_object_or_404(Wishlist, user=profile)
    print(wishlist)
    wishlist_item = get_list_or_404(WishlistItem, wishlist=wishlist)
    print(wishlist_item)
    print(type(wishlist_item))

    redirect_url = request.POST.get('redirect_url')

    product_added_item = get_object_or_404(Product, pk=product_id)
    wishlist_item.append(product_added_item)
    print(wishlist_item)
    wishlist.wishlist_item = wishlist_item

    return redirect(redirect_url)

