from tastypie.api import Api
from django.conf.urls import patterns, include, url

from polls.api import PollResource, ChoiceResource, VoteResource

from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(PollResource())
v1_api.register(ChoiceResource())
v1_api.register(VoteResource())

urlpatterns = patterns('',
    url(r'^', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
