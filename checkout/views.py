from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm
# Create your views here.


def checkout(request, item_id):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "No items in your bag")
        return redirect(reverse('products'))

    print(bag)
    order_form = OrderForm()
    template = '/checkout/checkout.html'
    context = {
        'Order_form': order_form
    }
    return render(request, template, context)
