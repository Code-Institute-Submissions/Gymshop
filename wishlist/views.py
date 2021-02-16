from django.shortcuts import render, redirect, reverse, HttpResponse, get_list_or_404, get_object_or_404

from .models import Product, UserProfile, Wishlist, WishlistItem

from django.contrib.auth.decorators import login_required

from django.utils import timezone

from django.contrib import messages


@login_required
def wishlist(request):
    """ A view to return the Wishlist """
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.get_or_create(user=user)

    products = WishlistItems.objects.all(wishlist=user)

    return render(request, 'wishlist/wishlist.html')


@login_required
def add_to_wishlist(request, product_id):
    """ A view to delete a item in the Wishlist """
    redirect_url = request.POST.get('redirect_url')

    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.get_or_create(user=user)
    wishlist_user = wishlist[0]

    product = Product.objects.get(pk=product_id)

    if WishlistItem.objects.get(wishlist=wishlist_user, product=product):
        messages.error(request, "Product is already in wishlist")
    else:
        variable = WishlistItem(wishlist=wishlist_user, product=product, date_added=timezone.now())
        variable.save()

    return redirect(redirect_url)


# @login_required
# def delete_from_wishlist(request, product_id):
#     redirect_url = request.POST.get('redirect_url')
#     return redirect(redirect_url)
