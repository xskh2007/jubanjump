# ~*~ coding: utf-8 ~*~

from __future__ import absolute_import, unicode_literals
from django import forms

from django.forms.models import ModelChoiceField
# from .models import MongoScript,MongoDbs

from django.forms import ModelForm

#
# class MongoScriptForm(ModelForm):
#     # part = ModelChoiceField(queryset=MongoScript.objects.all())
#     dbname = forms.ChoiceField(choices=[(doc.id,doc.dbname) for doc in MongoDbs.objects.all()])
#
#     class Meta:
#         model = MongoScript
#         widgets = {
#             'dbname': forms.Select(attrs={'class': 'select'}),
#         }
#         fields = '__all__'


