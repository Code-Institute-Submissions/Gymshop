from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from django.contrib import messages

# Create your views here.


def view_bag(request):
    """ A vie to return the shopping bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    item = get_object_or_404(Product, pk=item_id)
    if quantity > item.stock:
        messages.error(request,'You can not order more than what we have in stock!')
    else:
        item.stock -= quantity
        item.save()
        if item_id in list(bag.keys()):
            bag[item_id] += quantity

        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
