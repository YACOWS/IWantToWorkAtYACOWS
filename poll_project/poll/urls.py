# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

from piston.resource import Resource
from .handlers import PollHandler

poll_resource = Resource(handler=PollHandler)


urlpatterns = patterns('',
    url(r'^polls/(?P<poll_id>[^/]+)/$', poll_resource, name='poll'),
    url(r'^polls/$', poll_resource, name='polls'),
)

