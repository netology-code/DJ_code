from django.shortcuts import render

from demo.models import Order


def list_orders(request):
    orders = Order.objects.filter(positions__product__price__lte=600)
    context = {'orders': orders}
    return render(request, 'orders.html', context)
