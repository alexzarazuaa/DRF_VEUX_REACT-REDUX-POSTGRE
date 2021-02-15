from django.apps import AppConfig


class BarsAppConfig(AppConfig):
    name = 'bars'
    label = 'bars'
    verbose_name = 'Bars'

    def ready(self):
        import bars.signals

default_app_config = 'bars.BarsAppConfig'
