from django.shortcuts import render, redirect

from .models import Product, UserComments, UserProfile

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def add_comment(request, product_id):
    redirect_url = request.POST.get('redirect_url')

    user = request.user
    product = Product.objects.get(pk=product_id)
    comment = request.POST.get('comment')

    submission = UserComments(user=user, product=product, comment=comment)
    submission.save()
    return redirect(redirect_url)


def remove_comment(request, product_id):
    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)
