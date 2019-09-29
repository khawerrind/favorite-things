from django.apps import AppConfig


class FavoriteThingsAppConfig(AppConfig):
    name = 'api.apps.favorite_things'

    def ready(self):
        # Every time server restarts
        import api.apps.favorite_things.signals  # noqa
