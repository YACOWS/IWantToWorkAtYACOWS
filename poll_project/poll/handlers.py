# -*- coding: utf-8 -*-
from piston.handler import BaseHandler
from piston.utils import rc

from .models import Choice, Poll


class PollHandler(BaseHandler):
    allowed_methods = ('GET', 'POST',)
    model = Poll
    fields = ('id', 'question', ('choices', ('id', 'description', 'votes', )))

    def read(self, request, poll_id=None):
        if poll_id:
            return Poll.objects.get(pk=poll_id)
        else:
            return Poll.objects.all()

    def create(self, request):
        data = request.data
        choice = Choice.objects.get(pk=int(data['choice']))
        choice.vote()
        return rc.CREATED
