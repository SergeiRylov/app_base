## Добавление зависимости в `requirements.txt`

Добавьте пакет отдельной строкой, например:

```txt
Django==6.1.1
app_base @ git+https://github.com/SergeiRylov/app_base.git # add this
```

Установите зависимости командой:

```bash
pip install -r requirements.txt
```
