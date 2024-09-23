from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def catalog(request: HttpRequest):
    return render(request=request, template_name="goods_templates/catalog.html")


def product(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="goods_templates/product.html")
