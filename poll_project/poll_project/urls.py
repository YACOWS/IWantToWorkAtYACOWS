# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin

from poll.views import PollList


admin.autodiscover()

urlpatterns = patterns('',
    (r'^api/', include('poll.urls')),
    url(r'^polls/$', PollList.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
