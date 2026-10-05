"""urls settings"""

import os

from django.conf import settings
from django.urls import path
from django.views.generic.base import RedirectView

from app_base import views

app_name = "app_base"


def logo_url():
    if hasattr(settings, "LOGO_PATH") and os.path.isfile(os.path.join(settings.STATIC_ROOT, settings.LOGO_PATH)):
        return f"{settings.STATIC_URL}{settings.LOGO_PATH}"
    elif os.path.isfile(os.path.join(settings.STATIC_ROOT, "images", "logo.png")):
        return f"{settings.STATIC_URL}images/logo.png"
    else:
        return f"{settings.STATIC_URL}images/default/logo.png"


def favicon_url():
    if hasattr(settings, "FAVICON_PATH") and os.path.isfile(os.path.join(settings.STATIC_ROOT, settings.FAVICON_PATH)):
        return f"{settings.STATIC_URL}{settings.FAVICON_PATH}"
    elif os.path.isfile(os.path.join(settings.STATIC_ROOT, "favicon.ico")):
        return f"{settings.STATIC_URL}favicon.ico"
    else:
        return f"{settings.STATIC_URL}images/default/favicon.ico"


def apple_touch_icon_url():
    if hasattr(settings, "APPLE_TOUCH_ICON_PATH") and os.path.isfile(os.path.join(settings.STATIC_ROOT, settings.APPLE_TOUCH_ICON_PATH)):
        return f"{settings.STATIC_URL}{settings.APPLE_TOUCH_ICON_PATH}"
    elif os.path.isfile(os.path.join(settings.STATIC_ROOT, "apple-touch-icon.png")):
        return f"{settings.STATIC_URL}apple-touch-icon.png"
    else:
        return f"{settings.STATIC_URL}images/default/apple-touch-icon.png"


urlpatterns = [
    path("favicon.ico", RedirectView.as_view(url=favicon_url(), permanent=True), name="favicon.ico"),
    path("logo.png", RedirectView.as_view(url=logo_url(), permanent=True), name="logo.png"),
    path("apple-touch-icon.png", RedirectView.as_view(url=apple_touch_icon_url(), permanent=True), name="apple-touch-icon.png"),
    path("login-modal/", views.login_modal, name="login-modal"),
    path("accounts/login/", views.login_page, name="login-page"),
    path("logout/", views.logout, name="logout"),
    path("error-page-test/", views.error_test),
    path("", views.index, name="index"),
]
