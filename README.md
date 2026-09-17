# app_base

**app_base** — pip-пакет, реализующий базовый функционал и шаблоны для сайта на Django с использованием AdminLTE4 (bootstrap admin template)

## Функционал

### Базовый шаблон

Формирует базовый шаблон страницы с подключением необходимых css и js

```django
{% extends 'app_base/page.html'}

{% block css %}
{% endblock css %}

{% block page %}
{% endblock page %}

{% block js %}
{% endblock js %}
```

### Шаблоны для формирования полей форм

Формирует html код для поля формы, включая название поля, отметку required, вывод подписи или сообщения об ошибке

Доступны для следующих типов

- date
- input
- select
- select2 (by TomSelect)
- select2m (multiply values by TomSelect)
- textarea 
- time

```django
{% include 'app_base/forms/input.html' with field=form.user_name_eng %}
```

При вызове из каталога `forms/str/*` выводится только поле формы без label и обрамления

```django
{% include 'app_base/forms/str/input.html' with field=form.user_name_eng %}
```

### Модальные окна

To be continue ...
