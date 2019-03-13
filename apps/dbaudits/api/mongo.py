# -*- coding: utf-8 -*-
#
from rest_framework import viewsets
from django.db import transaction

from common.permissions import IsValidUser
from ..models import MongoSubmit
from ..serializers import MongoSubmitSerializer
from django.urls import reverse_lazy, reverse
from rest_framework_bulk import BulkModelViewSet
from common.mixins import IDInFilterMixin

from rest_framework.pagination import LimitOffsetPagination

from common.permissions import AdminUserRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView,View
from django.http import HttpResponse



class MongoSubmitViewSet(IDInFilterMixin, BulkModelViewSet):
    serializer_class = MongoSubmitSerializer
    permission_classes = (IsValidUser,)
    queryset = MongoSubmit.objects.all()
    success_url = reverse_lazy('users:user-list')
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return MongoSubmit.objects.all()

    def allow_bulk_destroy(self, qs, filtered):
        return qs.count() != filtered.count()
    #
    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #     instance.user = self.request.user
    #     instance.save()
    #     transaction.on_commit(lambda: run_command_execution.apply_async(
    #         args=(instance.id,), task_id=str(instance.id)
    #     ))


class MongoExecuteView(AdminUserRequiredMixin, View):
    def get(self, request):
        print(request.GET.get("env"))
        env = request.GET.get("env")
        # deployjenkins.delay(env)

        msg = """
        deploy ing ...
        """
        return HttpResponse(msg)