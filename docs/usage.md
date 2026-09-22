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

Убедитесь, что приложение добавлено в `INSTALLED_APPS`, а параметр `APP_DIRS` включён, если шаблон находится в каталоге приложения.

### Замена элементов базового шаблона

...

### Шаблоны для полей форм


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




