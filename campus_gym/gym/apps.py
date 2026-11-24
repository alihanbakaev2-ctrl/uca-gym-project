from django.apps import AppConfig


class GymConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gym'

    def ready(self):
        from django.db.models.signals import post_migrate

        def _sync(sender, **kwargs):
            from .library import sync_library

            sync_library()

        post_migrate.connect(_sync, sender=self)
