# -*- coding: utf-8 -*-
#

from django.utils.translation import ugettext as _
from django.conf import settings
from django.views.generic import ListView, TemplateView
from ..models import MongoSubmit
from common.permissions import AdminUserRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import (
    CreateView, UpdateView, FormView
)

from ..forms import MngoSubmitForm
from django.urls import reverse_lazy, reverse


__all__ = [
    'MngoSubmitView','MongoListView'
]



class MngoSubmitView(AdminUserRequiredMixin, SuccessMessageMixin, CreateView):
    model = MongoSubmit
    template_name = 'mongo/mongo_submit.html'
    form_class = MngoSubmitForm
    success_url = reverse_lazy("dbaudits:mongo-list")

    def form_valid(self, form):
        mongosubmit = form.save(commit=False)
        mongosubmit.created_by = self.request.user.username
        mongosubmit.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Ops'),
            'action': _('Command execution'),
            # 'form': self.get_form()
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class MongoListView(AdminUserRequiredMixin, TemplateView):

    template_name = 'mongo/mongo_list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'app': "数据库审计",
            'action': "mongo脚本记录",
        })
        return context


