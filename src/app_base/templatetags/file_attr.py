from pathlib import Path

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="file_name")
def file_name(value):
    """Возвращает имя файла без пути"""

    try:
        return Path(value.path).name
    except Exception as _:
        return None


@register.filter(name="file_size")
def file_size(value):
    """Возвращает размер файла"""

    try:
        return value.size
    except Exception as _:
        return None


@register.filter(name="file_icon")
def file_icon(value):
    """Преобразование в строку для сравнения в шаблоне формы select."""

    """
    Возвращает HTML-код иконки Bootstrap для указанного файла.
    Для использования в Django шаблонах.
    
    Args:
        file_path (str): Путь к файлу или папке
        
    Returns:
        str: Готовый HTML-код иконки (безопасный для вывода)
    
    Example:
        В шаблоне: {{ file.name|file_icon }}
        Или: {{ file.get_icon }}
    """

    # Получаем расширение файла
    try:
        ext = Path(value.path).suffix.lower()
    except Exception as _:
        return None

    # Словарь расширений -> иконки
    icon_map = {
        # Изображения
        ".jpg": "file-image",
        ".jpeg": "file-image",
        ".png": "file-image",
        ".gif": "file-image",
        ".svg": "file-image",
        ".webp": "file-image",
        ".bmp": "file-image",
        ".ico": "file-image",
        # Документы
        ".pdf": "file-pdf",
        ".doc": "file-word",
        ".docx": "file-word",
        ".txt": "file-text",
        ".rtf": "file-text",
        ".md": "file-text",
        # Таблицы
        ".xls": "file-excel",
        ".xlsx": "file-excel",
        ".csv": "file-excel",
        ".ods": "file-excel",
        # Презентации
        ".ppt": "file-ppt",
        ".pptx": "file-ppt",
        ".odp": "file-ppt",
        # Архивы
        ".zip": "file-zip",
        ".rar": "file-zip",
        ".7z": "file-zip",
        ".tar": "file-zip",
        ".gz": "file-zip",
        # Код
        ".py": "file-code",
        ".js": "file-code",
        ".html": "file-code",
        ".css": "file-code",
        ".json": "file-code",
        ".xml": "file-code",
        ".php": "file-code",
        ".java": "file-code",
        ".cpp": "file-code",
        ".c": "file-code",
        ".go": "file-code",
        ".rb": "file-code",
        ".sh": "file-code",
        # Видео
        ".mp4": "file-play",
        ".avi": "file-play",
        ".mkv": "file-play",
        ".mov": "file-play",
        ".webm": "file-play",
        # Аудио
        ".mp3": "file-music",
        ".wav": "file-music",
        ".flac": "file-music",
        ".aac": "file-music",
        # Системные
        ".exe": "file-exe",
        ".msi": "file-exe",
        ".dll": "file-exe",
        ".iso": "file-cd",
    }

    icon = icon_map.get(ext, "file")

    html = f'<i class="bi bi-{icon} width="64" height="64""></i>'
    return mark_safe(html)
