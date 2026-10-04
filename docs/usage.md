# Использование

## Базовый шаблон

### Замена базового шаблона

1. Создайте файл `templates/app_base/page.html` в приложении с
2. Укажите этот каталог в `TEMPLATES[0]['DIRS']` в `settings.py`:

   ```python
   TEMPLATES = [
       {
           # ...
           "DIRS": [BASE_DIR / "templates"],
       },
   ]
   ```

3. В дочернем шаблоне унаследуйте базовый и переопределите нужные блоки:

```django
    {% extends "page.html" %}

    {% block css %}{% endblock css %}

    {% block title %}Главная{% endblock title %}

    {% block page %}
    <h1>Главная страница</h1>
    {% endblock %}

    {% block js %}{% endblock js %}
```

### Замена элементов базового шаблона

#### favicon.ico, logo.png, apple-touch-icon.png

Для использования собственного логотипа:

**Вариант 1**.  

Укажите расположение файлов в файле 'settings.py' в каталоге `static`

```python
FAVICON_PATH = "images/favicon.ico"
LOGO_PATH = "images/logo.png"
APPLE_TOUCH_ICON_PATH = "images/apple-touch-icon.png"
```

**Вариант 2**.  

Поместите файлы в соответствующие каталоги

- `favicon.ico` в каталог `/static/`
- `apple-touch-icon.png` в каталог `/static/`
- `logo.png` в каталог `/static/images/`

Сначала происходит проверка наличия переменных в файле `settings.py`,
потом проверяется наличие файлов в указанных каталогах.
Если проверка не дает результатов, используются файлы из каталога `images/default/`

### Замена названия сайта

По умолчанию название сайта `wiki portal`

Для замены названия сайта создайте файл в каталоге
`templates/app_base/layout/class/site_name.txt`

```text
<site name>
```

## Шаблоны для полей форм

Формируют html код для поля формы, включая название поля, отметку required, вывод подписи или сообщения об ошибке

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

## Модальные окна

To be continue ...
