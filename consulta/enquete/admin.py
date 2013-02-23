# -*- coding: utf-8 -*-

from django.contrib import admin
from consulta.enquete.models import Enquete, Opcao

class EnqueteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Enquete, EnqueteAdmin)

class OpcaoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Opcao, OpcaoAdmin)
