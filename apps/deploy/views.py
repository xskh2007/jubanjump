from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
# from .models import MongoScript
from . import forms
from common.const import create_success_msg
from django.urls import reverse_lazy

from django.utils.translation import ugettext as _
from django.conf import settings
from django.views.generic import ListView, DetailView, TemplateView,View
from django.http import HttpResponse

from common.mixins import DatetimeSearchMixin
# from .models import Task, AdHoc, AdHocRunHistory, CeleryTask

from common.permissions import AdminUserRequiredMixin


from .tasks import deployjenkins

class DeployOnekeyView(AdminUserRequiredMixin,View):
    def get(self, request):
        print (request.GET.get("env"))
        env=request.GET.get("env")
        deployjenkins.delay(env)

        msg = """
        deploy ing ...
        """
        return HttpResponse(msg)


class DeployIndexView(AdminUserRequiredMixin, TemplateView):
    template_name = 'deploy/deploy_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'app': "发布管理",
            'action': "一键发布",
        })

        return context


from django.views.generic import CreateView
# from .forms import MongoScriptForm

# class MongoScriptCreate(CreateView):
#     form_class = MongoScriptForm
#     template_name = 'deploy/mongo_index.html'
#     success_url = reverse_lazy('deploy:deployindex')
#
#     def form_invalid(self, form):
#         return HttpResponse("form is invalid.. this is just an HttpResponse object")

# class MongoIndexView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
#
#     model = MongoScript
#     form_class = forms.MongoScriptForm
#     template_name = 'deploy/mongo_index.html'
#     success_url = reverse_lazy('deploy:mongoindex')
#     success_message = create_success_msg
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update({
#             'app': "发布管理",
#             'action': "mongo脚本提交",
#         })
#
#         return context