from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ A vie to return the shopping bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    item = get_object_or_404(Product, pk=item_id)
    if quantity > item.stock:
        messages.error(request, f'You can not order more than the {product.stock} item(s) we have in stock!')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'{product.name} quantity updated')

        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust a quantity of the specified product to the shopping bag """
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    item = get_object_or_404(Product, pk=item_id)
    if quantity > item.stock:
        messages.error(request, f'You can not order more than the {product.stock} item(s) we have in stock!')

    elif quantity <= int("0"):
        del bag[item_id]
        messages.success(request, f'{product.name} Successfully Removed')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] = quantity
            request.session['bag'] = bag
            messages.success(request, f'{product.name} quantity updated')

        else:
            bag[item_id] = quantity
            messages.success(request, f'{product.name} quantity updated')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Adjust a quantity of the specified product to the shopping bag """
    try:
        product = Product.objects.get(pk=item_id)
        bag = request.session.get('bag', {})

        if item_id in list(bag.keys()):
            del bag[item_id]
            request.session['bag'] = bag
            messages.success(request, f'{product.name} Successfully Removed')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error: {e}')
        return HttpResponse(status=500)
