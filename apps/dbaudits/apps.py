from __future__ import unicode_literals

from django.apps import AppConfig


class DbauditsConfig(AppConfig):
    name = 'dbaudits'

    def ready(self):
        # from . import signals_handler
        super().ready()
