from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from .models import Product
from .forms import OrderForm
from bag.views import view_bag
# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "No items in your bag")
        return redirect(reverse('products'))

    for item, value in bag.items():
        items = get_object_or_404(Product, pk=item)
        quantity = value
        if items.stock - quantity <= 0:
            messages.error(request,f'Stock for {items.name} changed since you last added items to your bag. We only have {items.stock} left')
            return redirect('view_bag')

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form
    }
    return render(request, template, context)
