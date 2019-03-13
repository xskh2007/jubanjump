# -*- coding: utf-8 -*-
#
import uuid
import json

from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.db import models



class MongoSubmit(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=128, verbose_name=_('title'), default="")
    dbname = models.CharField(max_length=128, verbose_name=_('dbname'),default="")
    script = models.TextField(verbose_name="Script")
    status = models.TextField(blank=True, null=True, verbose_name='Status')
    created_by = models.CharField(max_length=30, default='', verbose_name=_('Created by'))
    date_created = models.DateTimeField(auto_now_add=True)
    date_start = models.DateTimeField(null=True)
    date_finished = models.DateTimeField(null=True)

    def __str__(self):
        return self.script[:10]