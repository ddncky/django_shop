from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_list_or_404, render
from . models import Product


def catalog(request: HttpRequest, category_slug):
    if category_slug == "all":
        goods = Product.objects.all()
    else:
        goods = get_list_or_404(Product.objects.filter(category__slug=category_slug))

    context = {
        "title": "Home - Каталог",
        "goods": goods
    }
    return render(request=request, template_name="goods_templates/catalog.html", context=context)


def product(request: HttpRequest, product_slug) -> HttpResponse:
    product = Product.objects.get(slug=product_slug)

    context = {
        "product": product
    }
    return render(request=request, template_name="goods_templates/product.html", context=context)
