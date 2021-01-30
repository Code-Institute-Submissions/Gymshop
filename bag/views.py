from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ A vie to return the shopping bag """

    return render(request, 'bag/bag.html')
