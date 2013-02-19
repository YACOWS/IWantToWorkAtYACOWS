# -*- coding: utf-8 -*-
from django.db import models

'''
    classe opcaos da enquete
'''
class Opcoes(models.Model):
    data_criacao = models.DateTimeField( auto_now_add=True )
    descricao = models.CharField( (u'Opcao'), max_length=50, null=False, blank=False )

    class Meta:
        verbose_name = (u'Opção')
        verbose_name_plural = (u'Opções')

    def __unicode__(self):
        return u'%s' % self.descricao 

'''
    classe enquete
'''
class Enquete(models.Model):
    data_criacao = models.DateTimeField( auto_now_add=True )
    pergunta = models.CharField( (u'Pergunta'), max_length=50, null=False, blank=False )
    descricao = models.TextField( (u'Descrição'), null=True, blank=True )
    ativo = models.BooleanField( (u'Ativo?'), default=True )

    # fk
    opcoes = models.ManyToManyField(Opcoes, null=True, blank=True)

    class Meta:
        verbose_name = (u'Enquete')
        verbose_name_plural = (u'Enquetes')

    def __unicode__(self):
        return u'%s - %s' % ( self.pergunta, self.data_criacao )
