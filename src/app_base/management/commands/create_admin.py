from django.contrib.auth.models import User
from django.core.management.app_base import app_baseCommand


class Command(app_baseCommand):
    help = "Создание администратора"

    def add_arguments(self, parser):
        parser.add_argument("passwd",  nargs="?", default="admin", type=str)

    def handle(self, *args, **options):
        
        passwd = options["passwd"]
        if User.objects.filter(username="admin").exists():
            self.stdout.write(self.style.WARNING("Пользователь admin уже существует"))
        else:
            if passwd in ["", " ", None]:
                self.stdout.write(self.style.ERROR("Пароль не может быть пустым"))
            else:
                User.objects.create_superuser("admin", "admin@localhost", passwd)
                self.stdout.write(self.style.SUCCESS("Пользователь admin создан"))

