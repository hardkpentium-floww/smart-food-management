from django.apps import AppConfig

class MealsAppConfig(AppConfig):
    name = "meals"

    def ready(self):
        from meals import signals # pylint: disable=unused-variable
