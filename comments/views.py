from django.shortcuts import render, redirect, get_object_or_404

from .models import Product, UserComments, UserProfile

from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.


@login_required
def add_comment(request, product_id):
    """ A view to add a comment to a product """

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
        messages.error(request, "No such URL exists")
        return render(request, 'home/index.html')

@login_required
def remove_comment(request, product_id):
    """ A view to delete a comment """
    redirect_url = request.POST.get('redirect_url')
    if request.POST:
        user = UserProfile.objects.get(user=request.user)
        product = Product.objects.get(pk=product_id)

        test = UserComments.objects.filter(user=user, product=product).exists()

        if test:
            deleted_obj = UserComments.objects.get(user=user, product=product)
            deleted_obj.delete()
            messages.success(request, "Your comment was successfully deleted.")
        else:
            messages.error(request, "Error - No such comment exists")

        return redirect(redirect_url)

    else:
        messages.error(request, "No such URL exists")
        return render(request, 'home/index.html')
