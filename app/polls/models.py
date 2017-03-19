from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    
    def __unicode__(self):
        return self.question
        
    def total_votes(self):
        return sum(c.votes for c in self.choice_set.all())
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice