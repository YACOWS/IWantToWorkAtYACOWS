# from django.conf.urls.defaults import patterns, url, include
# from django.views.generic.simple import direct_to_template

# urlpatterns = patterns('',
#     url(r'^$', 'polls.views.list', name='polls_list'),
#     url(r'^(?P<poll_id>\d+)/$', 'polls.views.detail', name='polls_detail'),
# )

from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from polls.models import Poll

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date'),
            context_object_name='polls',
            template_name='polls/poll_list.html')),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/poll_detail.html'),
        name='poll_detail'),
    url(r'^(?P<pk>\d+)/vote/$', 'polls.views.vote', name='poll_vote'),
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/poll_results.html'),
        name='poll_results'),
)