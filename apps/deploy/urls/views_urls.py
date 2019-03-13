# ~*~ coding: utf-8 ~*~
from __future__ import unicode_literals


from django.conf.urls import url
from .. import views

__all__ = ["urlpatterns"]

app_name = "deploy"

urlpatterns = [
    #  deploy url
    url(r'^deploy/$', views.DeployIndexView.as_view(), name='deployindex'),
    url(r'^deployonekey/$', views.DeployOnekeyView.as_view(), name='deployonekey'),
    # url(r'^mongoindex/$', views.MongoIndexView.as_view(), name='mongoindex'),
    # url(r'^mongoscriptcreate/$', views.MongoScriptCreate.as_view(), name='mongoscriptcreate'),

]
