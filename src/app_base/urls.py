""" """

from django.urls import path

from app_base import views

app_name = "app_base"

urlpatterns = [
    path("", views.index, name="index"),
    path("login-modal/", views.login_modal, name="login-modal"),
    path("accounts/login/", views.login_page, name="login-page"),
    path("logout/", views.logout, name="logout"),
    path("error-page-test/", views.error_test),
]
