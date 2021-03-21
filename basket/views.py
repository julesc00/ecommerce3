from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .basket import Basket
from store.models import Product


def basket_summary(request):
    basket = Basket(request)
    context = {"basket": basket}

    return render(request, "store/basket/summary.html", context)


def basket_add(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("productId"))
        product_qty = int(request.POST.get("productQty"))
        product = get_object_or_404(Product, id=product_id)

        basket.add(product=product, qty=product_qty)
        basket_qty = basket.__len__()

        response = JsonResponse({"qty": basket_qty})

        return response


def basket_delete(request):
    pass
