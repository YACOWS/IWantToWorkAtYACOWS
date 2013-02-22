# -*- coding: utf-8 -*-
from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=255)

    def __unicode__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    description = models.CharField(max_length=255)
    votes = models.IntegerField(null=False, default=0)

    def __unicode__(self):
        return self.description

    def vote(self):
        self.votes = self.votes + 1
        self.save()
