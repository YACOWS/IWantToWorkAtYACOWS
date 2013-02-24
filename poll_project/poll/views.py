# -*- coding: utf-8 -*-
from django.views.generic import ListView
from .models import Poll


class PollList(ListView):
    model = Poll

