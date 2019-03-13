# ~*~ coding: utf-8 ~*~
from __future__ import unicode_literals

from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_bulk.routes import BulkRouter
from .. import api


app_name = "dbaudits"

router = BulkRouter()
router.register(r'mongosubmit', api.MongoSubmitViewSet, 'mongosubmit')


urlpatterns = [
    path('mongo-execute', api.MongoExecuteView.as_view(), name='mongo-execute'),
]

urlpatterns += router.urls
