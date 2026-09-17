from django import template

"""It's sometimes really handy to be able to do basic arithmetic in
Django templates.
"""


register = template.Library()


@register.filter
def to_str(value):
    """Преобразование значения в строку."""
    try:
        return str(value)
    except Exception as _e:
        return value


@register.filter
def subtract(value, arg):
    """Вычитание двух чисел."""

    try:
        return value - arg
    except Exception as _e:
        return value


@register.filter
def add(value, arg):
    """Сложение двух чисел."""

    try:
        return value + arg
    except Exception as _e:
        return value


@register.filter
def negative(value):
    """Возвращает отрицательное значение числа."""

    try:
        return -value
    except Exception as _e:
        return value
