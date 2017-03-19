from django.shortcuts import render
from django.utils import simplejson
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from polls.models import Choice, Poll
from polls.forms import PollVoteForm

def home(request):
    context = {'polls': Poll.objects.all()}
    
    return render(request, 'home.html', context)

def poll(request, poll_id):
    if request.method == 'POST':
        choice = Choice.objects.get(id=request.POST['vote'])
        choice.votes += 1
        choice.save()
        
        return HttpResponseRedirect(reverse('polls.views.poll', args=[poll_id,]))
    
    poll = Poll.objects.get(pk=poll_id)
    form = PollVoteForm(poll=poll)
    
    return render(request, 'poll.html', {'poll': poll, 'form': form})

def get_polls(request):
    polls = Poll.objects.all()
    json = []

    for poll in polls:
        choices = []

        for choice in poll.choice_set.all():
            choices.append({'id': choice.id, 'opcao': choice})

        tmp_json = {
            'id': poll.id,
            'enquete': poll.question,
            'criada_em': str(poll.created_at),
            'opcoes': str(choices),
            'votos': poll.total_votes()
        }
        json.append(tmp_json)

    return HttpResponse(simplejson.dumps(json), mimetype='application/json')

def save_poll(request):
    if not request.GET.get('poll_id'):
        json = {'status': 'Falha ao enviar o voto, especifique a enquete e tente novamente'}
        return HttpResponse(simplejson.dumps(json), mimetype='application/json')

    if not request.GET.get('choice_id'):
        json = {'status': 'Falha ao enviar o voto, especifique a opcao e tente novamente'}
        return HttpResponse(simplejson.dumps(json), mimetype='application/json')

    poll = Poll.objects.get(pk=request.GET.get('poll_id'))

    choice = Choice.objects.get(id=request.GET.get('choice_id'))
    choice.votes += 1
    choice.save()

    poll.save()
        
    json = {'status': 'Voto enviado com sucesso!'}
    return HttpResponse(simplejson.dumps(json), mimetype='application/json')
