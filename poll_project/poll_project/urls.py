# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin

from poll.views import PollList#, PollVoteView


admin.autodiscover()

urlpatterns = patterns('',
    (r'^api/', include('poll.urls')),
    url(r'^polls/$', PollList.as_view()),
    url(r'^polls/vote/(?P<poll_id>[^/]+)/$', 'poll.views.vote', name='vote'),
    url(r'^admin/', include(admin.site.urls)),
)
