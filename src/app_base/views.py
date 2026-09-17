from datetime import date, timedelta

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect, render
from django.urls import Resolver404, resolve
from django.utils.translation import gettext_lazy as _
from django.core.mail import mail_admins
from django.http import Http404

from app_base import forms



def index(request):
    """
    Главная страница
    """

    title = "Главная"
    breadcrumbs = [(None, title)]

    current_date = date.today()



    content = {
        "title": title,
        "breadcrumb": breadcrumbs,
    }

    return render(request, "app_base/index.html", content)




def login_modal(request):
    """Стандартный вход в систему"""

    form = forms.LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)


                return redirect(request.META["HTTP_REFERER"])
            else:
                messages.error(request, _("Invalid credentials"))
        else:
            messages.error(request, _("Error validating the form"))
        return redirect(request.META["HTTP_REFERER"])

    return render(request, "app_base/login-modal.html", {"form": form, "msg": msg})


def login_page(request):
    """Страница входа в систему"""

    if request.user.is_authenticated:
        return redirect("/")

    title = "Вход"
    breadcrumbs = [
        (None, title),
    ]

    form = forms.LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)


                url = request.GET.get("next", None)
                if url is not None:
                    try:
                        resolve(url)
                        return redirect(url)
                    except Resolver404:
                        pass
                return redirect("/")
            else:
                messages.error(request, "Некорректные учетные данные")
        else:
            messages.error(request, "Ошибка проверки формы")

    content = {
        "breadcrumbs": breadcrumbs,
        "form": form,
    }

    return render(request, "app_base/login-page.html", content)


# def password(request):
#     if request.POST:
#         form = forms.ChangePasswordForm(request.POST)
#         if form.is_valid():
#             user = request.user
#             if user.check_password(form.cleaned_data["password_old"]):
#                 user.set_password(form.cleaned_data["password_new"])
#                 user.save()
#                 return redirect("/")
#             else:
#                 form.add_error("password_old", _("Old password is incorrect"))
#     else:
#         form = forms.ChangePasswordForm()

#     content = {"form": form}
#     return render(request, "home/password.html", content)


def logout(request):
    """Выход из системы"""
    django_logout(request)
    return redirect("/")


def error_test(request):
    raise Http404("Страница не найдена")


def error_400(request, exception):
    message = f"{request.path} 400"
    mail_admins("Error 400", message, fail_silently=True, connection=None, html_message=None)

    content = {"error_title": _("Error 400"), "error_text": _("Bad request")}
    return render(request, "app_base/error-page.html", content)


def error_403(request, exception):
    message = f"{request.path} 403"
    mail_admins("Error 403", message, fail_silently=True, connection=None, html_message=None)

    content = {"error_title": _("Error 403"), "error_text": _("Permission denied")}
    return render(request, "app_base/error-page.html", content)


def error_404(request, exception):
    message = f"{request.path} 404"
    mail_admins("Error 404", message, fail_silently=True, connection=None, html_message=None)

    content = {"error_title": _("Error 404"), "error_text": _("Page not found")}
    return render(request, "app_base/error-page.html", content)


def error_500(request):
    content = {"error": _("Error 500")}
    return render(request, "app_base/error-page.html", content)
