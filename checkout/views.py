from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from .models import Product
from .forms import OrderForm
# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "No items in your bag")
        return redirect(reverse('products'))

    # for item, value in bag:
    #     items = get_object_or_404(Product, pk=item)
    #     quantity = value
    #     left_over_stock =items.stock - quantity
    #     if left_over_stock <= 0:
    #       messages.error("Stock has changed since you last added items to your bag")
    #       redirect
    #     else:
    #        |
    #       \ /
    #        


    print(bag)
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form
    }
    return render(request, template, context)
