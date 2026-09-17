from django import template

"""It's sometimes really handy to be able to do basic arithmetic in
Django templates.
"""


register = template.Library()


@register.filter
def add_class(field, css_class):
    """Добавляет класс к виджету поля."""
    try:
        return field.as_widget(attrs={"class": css_class})
    except Exception as _e:
        return field
