from django import template
from django.http import HttpRequest
from carts.models import Cart

register = template.Library()


@register.simple_tag()
def user_carts(request: HttpRequest):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)