from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from . models import Product


def catalog(request: HttpRequest):
    goods = Product.objects.all()
    context = {
        "title": "Home - Каталог",
        "goods": goods
    }
    return render(request=request, template_name="goods_templates/catalog.html", context=context)


def product(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="goods_templates/product.html")
