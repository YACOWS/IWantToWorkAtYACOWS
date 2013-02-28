from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from models import Poll

def vote(request, pk):

    poll = get_object_or_404(Poll, pk=pk)

    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        message = 'You must select a choice'

    else:
        selected_choice.vote()
        message = 'Your vote was sent!'

    return render_to_response('polls/poll_detail.html', {
        'poll': poll,
        'message': message
    }, context_instance=RequestContext(request))