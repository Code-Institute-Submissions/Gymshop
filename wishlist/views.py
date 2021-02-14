from django.shortcuts import render, redirect, reverse, HttpResponse, get_list_or_404, get_object_or_404


# Create your views here.


def wishlist(request):
    """ A view to return the shopping bag """

    return render(request, 'wishlist/wishlist.html')
