from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from goods.models import Category


def index(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.all()
    context = {
        "title": "Home - главная", 
        "content": "Магазин мебели HOME",
        "categories": categories
        }
    
    return render(request=request, template_name="main_templates/index.html", context=context)


def about(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Home - о нас", 
        "content": "О нас:",
        "text_on_page": "Наш магазин был создан в ходе написания Дмитрием обучающего проекта по фреймворку Django!"
        }
    
    return render(request=request, template_name="main_templates/about.html", context=context)


def delivery_and_payment(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Home - доставка и оплата", 
        "content": "Доставка и оплата осуществляются:",
        "text_on_page": "Если вы хотите заказать наш товар, то для начала подумайте о том, что потребление и деньги - зло!"
        }
    
    return render(request=request, template_name="main_templates/about.html", context=context)


def contact_info(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Home - контактная информация", 
        "content": "Наши адреса:",
        "text_on_page": "Улица Пушкина, дом Колотушкина. Телефон для связи: 333333333!"
        }
    
    return render(request=request, template_name="main_templates/about.html", context=context)