from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from . import models


class HomeView(TemplateView):
    template_name = 'home/home.html'
    context_object_name = 'home'
