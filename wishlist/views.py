from django.shortcuts import render, redirect, reverse

# Create your views here.


def wishlist(request):
    """ A view to return the shopping bag """

    return render(request, 'wishlist/wishlist.html')
