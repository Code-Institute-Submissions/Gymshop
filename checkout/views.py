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

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    for item, value in bag.items():
        items = get_object_or_404(Product, pk=item)
        quantity = value
        if items.stock - quantity < 0:
            messages.error(request,f'Stock for {items.name} changed since you last added items to your bag. We only have {items.stock} left')
            return redirect('view_bag')

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, "Stripe public key not set.")

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }
    return render(request, template, context)
