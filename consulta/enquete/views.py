# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, HttpResponse, redirect, get_object_or_404
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

