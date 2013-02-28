from tastypie import fields, utils
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication

from polls.models import Poll, Choice, Vote


class PollResource(ModelResource):
    choices = fields.ToManyField('polls.api.ChoiceResource', 'choice_set', full=True)

    class Meta:
        queryset = Poll.objects.all()
        resource_name = 'poll'
        allowed_methods = ['get']

class ChoiceResource(ModelResource):
    poll = fields.ForeignKey(PollResource, 'poll')

    class Meta:
        queryset = Choice.objects.all()
        resource_name = 'choice'
        allowed_methods = ['get']

    def dehydrate(self, bundle):
        bundle.data['votes'] = Choice.objects.get(pk=bundle.obj.id).votes()
        return bundle

class VoteResource(ModelResource):
    choice = fields.ForeignKey(ChoiceResource, 'choice')

    class Meta:
        queryset = Vote.objects.all()
        resource_name = 'vote'
        allowed_methods = ['get', 'post']
        authorization = Authorization()
        authentication = Authentication()
