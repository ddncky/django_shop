from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def login(request: HttpRequest):
    context = {
        "title": "Home - Авторизация"
    }
    return render(request=request, template_name="users_templates/login.html", context=context)


def registration(request: HttpRequest):
    context = {
        "title": "Home - Регистрация"
    }
    return render(request=request, template_name="users_templates/registration.html", context=context)


def profile(request: HttpRequest):
    context = {
        "title": "Home - Личный Кабинет"
    }
    return render(request=request, template_name="users_templates/profile.html", context=context)


def logout(request: HttpRequest):
    return render(request=request, template_name="")
    