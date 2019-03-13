from __future__ import unicode_literals

from django.apps import AppConfig


class DeployConfig(AppConfig):
    name = 'deploy'

    def ready(self):
        # from . import signals_handler
        super().ready()

