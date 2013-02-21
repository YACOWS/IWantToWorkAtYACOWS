from django.test import TestCase
from django.utils import timezone

from polls.models import Choice, Poll

class PollModelTestCase(TestCase):
    options = {'question': 'Test question!', 'created_at': timezone.now()}
    
    def test_create_a_poll_and_save_it_to_the_database(self):
        poll = Poll()
        poll.question = self.options.get('question')
        poll.created_at = self.options.get('created_at')
        
        poll.save()
        
        polls_list = Poll.objects.all()
        self.assertEquals(len(polls_list), 1)
        
        current_poll = polls_list[0]
        self.assertEquals(current_poll, poll)
        
        self.assertEquals(current_poll.question, self.options.get('question'))
        
        # TODO - stored value @ MySQL is not going with miliseconds
        # self.assertEquals(current_poll.created_at, poll.created_at)
        
    def test_poll_objects_are_named_according_to_its_name(self):
        poll = Poll()
        poll.question = self.options.get('question')
        
        self.assertEquals(unicode(poll), self.options.get('question'))
        
class ChoiceModelTest(TestCase):
    options = {
        'question': 'Test question!', 
        'created_at': timezone.now(), 
        'choice': 'Test choice', 
        'votes': 10
    }
    
    def test_create_poll_choices(self):
        poll = Poll()
        
        poll.question = self.options.get('question')
        poll.created_at = self.options.get('created_at')
        
        poll.save()
        
        choice = Choice()
        
        choice.poll = poll
        choice.choice = self.options.get('choice')
        choice.votes = self.options.get('votes')
        
        choice.save()
        
        poll_choices = poll.choice_set.all()
        self.assertEquals(poll_choices.count(), 1)
        
        choice_from_db = poll_choices[0]
        self.assertEquals(choice_from_db, choice)
        self.assertEquals(choice_from_db.choice, self.options.get('choice'))
        self.assertEquals(choice_from_db.votes, self.options.get('votes'))
        
    def test_default_choices(self):
        choice = Choice()
        self.assertEquals(choice.votes, 0)
        