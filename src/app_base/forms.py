from django import forms
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": _("username"), "class": "form-control"}
        ),
        label=_("Username or email"),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": _("password"), "class": "form-control"}
        ),
        label=_("Password"),
    )


class ChangePasswordForm(forms.Form):
    password_old = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": _("Current password"), "class": "form-control"}
        )
    )
    password_new = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": _("New password"), "class": "form-control"}
        )
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": _("Confirm password"), "class": "form-control"}
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        if new_password != confirm_password:
            raise forms.ValidationError(
                "New password and confirm password do not match"
            )
        return cleaned_data
