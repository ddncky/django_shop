from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Home", "content": "Главная страница магазина - HOME"
        }
    return render(request=request, template_name="main_templates/index.html", context=context)


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse("About page")
