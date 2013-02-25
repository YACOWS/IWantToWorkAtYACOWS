# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Choice, Poll


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    readonly_fields = ['votes', ]


class PollAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline, ]


admin.site.register(Poll, PollAdmin)
