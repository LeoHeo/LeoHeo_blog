from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    name = "users"

    def ready(self):
        from users.signals.post_save_user import post_save_user
