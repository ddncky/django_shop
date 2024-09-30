from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm


def login(request: HttpRequest):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, вы вошли в аккаунт.")
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {
        "title": "Home - Авторизация",
        "form": form,
    }

    return render(request=request, template_name="users_templates/login.html", context=context)


def registration(request: HttpRequest):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, вы успешно зарегестрированы и вошли в аккаунт.")
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()

    context = {
        "title": "Home - Регистрация",
        "form": form,
    }
    return render(request=request, template_name="users_templates/registration.html", context=context)


@login_required
def profile(request: HttpRequest):
    if request.method == "POST":
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"{request.user.username}, ваш профиль успешно обновлен.")
            return HttpResponseRedirect(reverse("user:profile"))
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        "title": "Home - Личный Кабинет",
        "form": form,
    }
    return render(request=request, template_name="users_templates/profile.html", context=context)


@login_required
def logout(request: HttpRequest):
    messages.success(request, f"{request.user.username}, вы успешно разлогинились.")
    auth.logout(request)
    return redirect(reverse("main:index"))
    