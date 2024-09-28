from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator
from . models import Product
from . utils import q_search


def catalog(request: HttpRequest, category_slug=None):
    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("q", None)

    if category_slug == "all":
        goods = Product.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Product.objects.filter(category__slug=category_slug)

    if on_sale:
        goods = goods.filter(discount__gt=0) # type: ignore

    if order_by and order_by != "default":
        goods = goods.order_by(order_by) # type: ignore

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
