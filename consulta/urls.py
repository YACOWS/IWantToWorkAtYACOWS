# -*- coding: utf-8 _-*-

from django.conf.urls.defaults import patterns, include, url
#from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail

from enquete.models import Enquete

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# todas as enquetes
enquete_todas = {
        "queryset" : Enquete.objects.all(),
        }

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'consulta.views.home', name='home'),
    # url(r'^consulta/', include('consulta.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^save/(?P<obj>\d+)/$', 'consulta.enquete.views.salvar'),  # salvar opcao escolhida

    #url('^$', direct_to_template, { 
                                    #'template': 'lista.html' 
                                    #})

    (r'^$', list_detail.object_list, enquete_todas )

)
