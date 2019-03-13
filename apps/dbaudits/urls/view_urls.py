# ~*~ coding: utf-8 ~*~
from __future__ import unicode_literals
from django.urls import path

from .. import views

__all__ = ["urlpatterns"]

app_name = "dbaudits"

urlpatterns = [
    # Resource Task url

    path('mongo-submit', views.MngoSubmitView.as_view(), name='mongo-submit'),
    path('mongo-list', views.MongoListView.as_view(), name='mongo-list'),
]
