# -*- coding: utf-8 -*-
from django.db import models
from consulta.utils import GenString

'''
    classe opcaos da enquete
    Tiago de Souza Moraes
    19.02.2013
'''
class Opcao(models.Model):
    data_criacao = models.DateTimeField( auto_now_add=True )
    descricao = models.CharField( (u'Opcao'), max_length=50, null=False, blank=False )
    votos = models.PositiveIntegerField( (u'Votos recebidos'), default=0 )

    class Meta:
        verbose_name = (u'Opção')
        verbose_name_plural = (u'Opções')

    def __unicode__(self):
        return u'%s' % self.descricao 

'''
    classe enquete
    Tiago de Souza Moraes
    19.02.2013
'''
class Enquete(models.Model):
    data_criacao = models.DateTimeField( auto_now_add=True )
    pergunta = models.CharField( (u'Pergunta'), max_length=50, null=False, blank=False )
    descricao = models.TextField( (u'Descrição'), null=True, blank=True )
    ativo = models.BooleanField( (u'Ativo?'), default=True )
    url = models.CharField( (u'URL'), max_length=50, null=False, blank=False )

    # fk
    opcoes = models.ManyToManyField(Opcao, null=True, blank=True)

    def save(self, *args, **kwargs):
        # gerar URL unica para cada enquete nova
        if not self.id :
            self.url = GenString(32)

    class Meta:
        verbose_name = (u'Enquete')
        verbose_name_plural = (u'Enquetes')

    def __unicode__(self):
        return u'%s - %s' % ( self.pergunta, self.data_criacao )
