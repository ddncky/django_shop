from struct import pack
from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator
from . models import Product


def catalog(request: HttpRequest, category_slug):
    page = request.GET.get("page", 1)

    if category_slug == "all":
        goods = Product.objects.all()
    else:
        goods = get_list_or_404(Product.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Home - Каталог",
        "goods": current_page,
        "slug_url": category_slug
    }
    return render(request=request, template_name="goods_templates/catalog.html", context=context)


def product(request: HttpRequest, product_slug) -> HttpResponse:
    product = Product.objects.get(slug=product_slug)

    context = {
        "product": product
    }
    return render(request=request, template_name="goods_templates/product.html", context=context)
