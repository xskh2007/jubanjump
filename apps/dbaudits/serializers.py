# -*- coding: utf-8 -*-
#

from rest_framework import serializers

from .models import MongoSubmit


class MongoSubmitSerializer(serializers.ModelSerializer):

    class Meta:
        model = MongoSubmit
        fields = '__all__'
