from django.contrib import auth
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm


def login(request: HttpRequest):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {
        "title": "Home - Авторизация",
        "form": form,
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
    