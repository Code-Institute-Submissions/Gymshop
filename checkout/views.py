from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from .models import Product
from .forms import OrderForm
from bag.contexts import bag_contents
import stripe
from django.conf import settings
from bag.views import view_bag
# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "No items in your bag")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)


    for item, value in bag.items():
        items = get_object_or_404(Product, pk=item)
        quantity = value
        if items.stock - quantity < 0:
            messages.error(request,f'Stock for {items.name} changed since you last added items to your bag. We only have {items.stock} left')
            return redirect('view_bag')

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IAvHVECTsEQEyp4uaa1Ygz9AQGg1As3mODsvFGRNI9RLcpPTPLv58rxFfRK1j831KYRBlETVze7VMlFI7qo2eIY00An40UxNo',
        'client_secret': 'test client secret'
    }
    return render(request, template, context)
