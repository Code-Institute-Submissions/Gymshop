from django.shortcuts import render, redirect

# Create your views here.


def add_comment(request, product_id):
    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)


def remove_comment(request, product_id):
    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)
