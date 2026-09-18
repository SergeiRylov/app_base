from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(name="enter_key_down")
def enter_key_down():
    """Возвращает скрипт для для отправки формы при нажатия Enter"""

    return mark_safe('onkeydown="if (event.keyCode == 13) { this.form.submit(); return false; }"')


@register.filter(name="to_str")
def to_str(value):
    """Преобразование в строку для сравнения в шаблоне формы select."""

    try:
        return str(value)
    except Exception as _:
        return value


@register.filter(name="to_int")
def to_int(value):
    """Преобразование в число для сравнения в шаблоне формы select."""

    try:
        return int(value)
    except Exception as _:  # noqa: BLE001
        return value


@register.filter(name="search_replace")
def search_replace(value, arg):
    """Замена текста в строке для подсветки строки поиска в шаблоне."""

    if not arg or not value:
        return value
    
    # Приводим к нижнему регистру
    value_lower = value.lower()
    arg_lower = arg.lower()
    
    # Ищем позицию
    num = value_lower.find(arg_lower)
    if num == -1:
        return value
    
    # Собираем
    end_pos = num + len(arg)
    result = f"{value[:num]}<span class='text-info'>{value[num:end_pos]}</span>{value[end_pos:]}"
    
    return mark_safe(result)


@register.filter(name="currency")
def currency_format(value):
    """Возвращает возвращает отформатированное число"""

    if value is None:
        return 0.0

    try:
        currency = f"{value:,.2f}".replace(",", " ").replace(".", ",")
    except Exception as _:
        currency = value

    return currency


@register.filter(name="timedelta_format")
def timedelta_format(value):
    """Возвращает возвращает timedelta в формате чч:мм"""

    if value is None:
        return "00:00"

    try:
        total_seconds = int(value.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        return f"{hours:02}:{minutes:02}"
    except Exception as _:
        return "00:00"


@register.simple_tag(name="get_param_set", takes_context=True)
def get_param_set(context, name=None, value=None):
    """Формирует GET запрос из текущих параметров и добавляет указанное значение"""

    params = dict(context["request"].GET.items())

    if name is None:
        # Параметр не указан, просто возвращаем строку
        pass
    elif value is None and name in params:
        # Значение не указано, удаляем параметр
        params.pop(name)
    else:
        # Добавляем параметр
        params[name] = value

    if params:
        link = "?{}".format("&".join(f"{n}={v}" for n, v in params.items()))
    else:
        return ""

    return mark_safe(link)
