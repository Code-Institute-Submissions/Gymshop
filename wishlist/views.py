from django.shortcuts import render, redirect, reverse

# Create your views here.

def wishlist(request):
    return redirect(reverse('products'))