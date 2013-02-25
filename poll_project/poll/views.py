# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.views.generic import ListView

from .forms import PollVoteForm
from .models import Choice, Poll


class PollList(ListView):
    model = Poll


def vote(request, poll_id):

    poll = Poll.objects.get(id=poll_id)

    if request.method == 'POST':
        form = PollVoteForm(data=request.POST, poll_id=poll_id)
        if form.is_valid():
            return redirect('/polls')
    else:
        form = PollVoteForm(poll_id=poll_id)

    return render_to_response('vote.html', {'form': form, 'poll': poll}, 
        context_instance=RequestContext(request))
