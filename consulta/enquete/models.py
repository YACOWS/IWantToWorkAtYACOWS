# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify

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
    url = models.CharField( (u'URL'), max_length=50, null=True, blank=True)

    # fk
    opcoes = models.ManyToManyField(Opcao, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.url = slugify(self.pergunta)
        super(Enquete, self).save(*args, **kwargs)

    class Meta:
        verbose_name = (u'Enquete')
        verbose_name_plural = (u'Enquetes')

    def __unicode__(self):
        return u'%s - %s' % ( self.pergunta, self.data_criacao )

    # retorna opcoes de voto em orderm alfabetica
    def opcoes_voto(self, *args, **kwargs):
        return Opcao.objects.filter(enquete=self).order_by('descricao')
