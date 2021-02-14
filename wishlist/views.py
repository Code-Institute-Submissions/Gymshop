from django.shortcuts import render, redirect, reverse, HttpResponse, get_list_or_404, get_object_or_404

from .models import Product, UserProfile, Wishlist

from django.contrib import messages

# Create your views here.


def wishlist(request):
    """ A view to return the shopping bag """

    return render(request, 'wishlist/wishlist.html', context)


def add_to_wishlist(request, product_id):


    return render(request, redirect_url)
