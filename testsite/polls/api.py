from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie import fields

from polls.models import Poll, Choice


class PollResource(ModelResource):
    class Meta:
        queryset = Poll.objects.all()
        authorization= Authorization()
        resource_name = 'poll'


class ChoiceResource(ModelResource):
    poll = fields.ForeignKey(PollResource, 'poll')

    class Meta:
        queryset = Choice.objects.all()
        authorization= Authorization()
        resource_name = 'choice'
