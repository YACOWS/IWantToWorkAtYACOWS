# -*- coding: utf-8 -*-
from piston.handler import BaseHandler

from .models import Poll


class PollHandler(BaseHandler):
    allowed_methods = ('GET', )
    model = Poll
    fields = ('id', 'question', ('choices', ('id', 'description', 'votes', )))

    def read(self, request, poll_id=None):
        if poll_id:
            return Poll.objects.get(pk=poll_id)
        else:
            return Poll.objects.all()

