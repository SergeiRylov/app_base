"""urls settings"""

import os

from django.conf import settings
from django.contrib.staticfiles import finders
from django.http import FileResponse
from django.urls import path

from app_base import views

app_name = "app_base"


def favicon_view(request):
    """Отдаем файл favicon.ico"""

    if hasattr(settings, "FAVICON_PATH") and os.path.isfile(
        os.path.join(settings.STATIC_ROOT, settings.FAVICON_PATH)
    ):
        file_path = os.path.join(settings.STATIC_ROOT, settings.FAVICON_PATH)
    elif os.path.isfile(os.path.join(settings.STATIC_ROOT, "favicon.ico")):
        file_path = os.path.join(settings.STATIC_ROOT, "favicon.ico")
    else:
        file_path = finders.find("images/default/favicon.ico")
    return FileResponse(open(file_path, "rb"), content_type="image/x-icon")


def apple_touch_icon_view(request):
    """Отдаем иконку для apple"""

    if hasattr(settings, "APPLE_TOUCH_ICON_PATH") and os.path.isfile(
        os.path.join(settings.STATIC_ROOT, settings.APPLE_TOUCH_ICON_PATH)
    ):
        file_path = os.path.join(settings.STATIC_ROOT, settings.FAVICON_PATH)
    elif os.path.isfile(os.path.join(settings.STATIC_ROOT, "apple-touch-icon.png")):
        file_path = os.path.join(settings.STATIC_ROOT, "apple-touch-icon.png")
    else:
        file_path = finders.find("images/default/apple-touch-icon.png")

    return FileResponse(open(file_path, "rb"), content_type="image/png")


def logo_view(request):
    """Отдаем логотип"""

    if hasattr(settings, "LOGO_PATH") and os.path.isfile(
        os.path.join(settings.STATIC_ROOT, settings.LOGO_PATH)
    ):
        file_path = os.path.join(settings.STATIC_ROOT, settings.FAVICON_PATH)
    elif os.path.isfile(os.path.join(settings.STATIC_ROOT, "logo.png")):
        file_path = os.path.join(settings.STATIC_ROOT, "logo.png")
    else:
        file_path = finders.find("images/default/logo.png")

    return FileResponse(open(file_path, "rb"), content_type="image/png")


urlpatterns = [
    path("favicon.ico", favicon_view),
    path("apple-touch-icon.png", apple_touch_icon_view),
    path("apple-touch-icon-precomposed.png", apple_touch_icon_view),
    path("logo.png", logo_view),
    path("login-modal/", views.login_modal, name="login-modal"),
    path("accounts/login/", views.login_page, name="login-page"),
    path("login/", views.login_only, name="login-only"),
    path("logout/", views.logout, name="logout"),
    path("error-page-test/", views.error_test),
    path("", views.index, name="index"),
]
