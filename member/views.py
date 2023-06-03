from django.shortcuts import redirect, render
from django.views.generic import ListView

from . import models


class MemberView(ListView):
    model = models.Member
    template_name = 'member/member.html'
    context_object_name = 'member'
