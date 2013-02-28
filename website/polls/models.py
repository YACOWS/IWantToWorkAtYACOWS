from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.choice_text

    def votes(self):
        return Vote.objects.filter(choice=self).count()
    votes.short_description = 'Votes'

    def vote(self):
        vote = Vote(choice=self)
        vote.save()

class Vote(models.Model):
    choice = models.ForeignKey(Choice)
