from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .basket import Basket
from store.models import Product


def basket_summary(request):

    context = {}
    return render(request, "store/basket/summary.html", context)


def basket_add(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("productId"))
        product_qty = int(request.POST.get("productQty"))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        response = JsonResponse({"qty": product_qty})

        return response
