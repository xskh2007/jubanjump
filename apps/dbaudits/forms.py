# ~*~ coding: utf-8 ~*~

from django import forms
from .models import MongoSubmit
from django.forms import ModelForm






class MngoSubmitForm(ModelForm):

    class Meta:
        model = MongoSubmit
        fields = [
            'title','dbname','script'
        ]

    def save(self, commit=True):
        is_finished = "1"
        MngoSubmit = super().save(commit=commit)
        MngoSubmit.is_finished = is_finished
        MngoSubmit.save()
        return MngoSubmit