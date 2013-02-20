# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, HttpResponse, redirect, get_object_or_404
from django.utils import simplejson

from consulta.enquete.models import Enquete, Opcao

'''
    Tiago de Souza Moraes
    monta opcao da enquete
    salva opcao selecinada e comuta voto

    url : Enquete.url
'''

def salvar(request, url=None):

    if not url == None:

        obj = get_object_or_404( Enquete, url=url )

        if request.POST:

            if not request.POST.get('opcao') == 'None' or request.POST.get('opcao') == None :

                opcao = Opcao.objects.get( pk=request.POST.get('opcao') )
                opcao.votos += 1
                opcao.save()
                msg = u'Voto comutado com sucesso!'

        return render_to_response('index.html', locals() )

    else:

        return redirect('/')


'''
    Tiago de Souza Moraes
    retorna todas as enquetes e suas opções em formato json
'''
def enquete_json( request ):

    array = {} # json
    i = 0


    for e in Enquete.objects.all():

        # opcoes da enquete
        tmp = []

        for o in e.opcoes.all() :
            tmp.append( [u'%s' % o, u'%s' % o.id] )

        array[i] = { 
           'enquete': '%s' % e.pergunta,
           'id': '%s' % e.id,
           'data_criaco': '%s' % e.data_criacao,
           'descricao': '%s' % e.descricao,
           'url': '%s' % e.url,
           'opcoes': tmp,
        }
        i += 1

    return HttpResponse(simplejson.dumps(array, sort_keys=True), mimetype='application/json')
