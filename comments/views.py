from django.shortcuts import render, redirect, get_object_or_404

from .models import Product, UserComments, UserProfile

from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.


@login_required
def add_comment(request, product_id):
    redirect_url = request.POST.get('redirect_url')

    product = Product.objects.get(pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)
    comment = request.POST.get('comment')
    if request.POST:
        test = UserComments.objects.filter(user=user, product=product).exists()
        if test:
            messages.error(request, "You have already commented.\
                Delete your comment and submit a new comment")

        else:
            submission = UserComments(user=user, product=product, comment=comment)
            submission.save()
            messages.success(request, "Successfully Commented")

        return redirect(redirect_url)
    else:
        messages.error(request, "Something went wrong try again")
        return render(request, 'home/index.html')


def remove_comment(request, product_id):
    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)
