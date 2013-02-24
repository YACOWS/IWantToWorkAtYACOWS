# -*- coding: utf-8 -*-
import json

from django.core.urlresolvers import reverse
from django.test import TestCase

from ..models import Poll, Choice


class PollAPITestCase(TestCase):

    def setUp(self):
        self.poll_1 = Poll.objects.create(question=u"What's the answer to the Ultimate Question of Life, The Universe, and Everything?")
        self.poll_1_choice_1 = Choice.objects.create(poll=self.poll_1, description=u'42')
        self.poll_1_choice_2 = Choice.objects.create(poll=self.poll_1, description=u'1')

        self.poll_2 = Poll.objects.create(question=u'What Is The Airspeed Velocity Of An Unladen Swallow?')
        self.poll_2_choice_1 = Choice.objects.create(poll=self.poll_2, description=u'What do you mean? An African or European swallow?')
        self.poll_2_choice_2 = Choice.objects.create(poll=self.poll_2, description=u'Huh? I... I don\'t know that.')

    def test_api_returns_valid_json(self):
        response = self.client.get(reverse('polls'))
        try:
            json_returned = json.loads(response.content)
        except ValueError:
            self.fail('Should be a valid JSON response.')
        
    def test_api_with_poll_id_return_json_of_specified_poll(self):
        expected_output = {
            'id': self.poll_1.id,
            'question': self.poll_1.question,
            'choices': [
                {
                    'votes': self.poll_1_choice_1.votes, 
                    'description': self.poll_1_choice_1.description, 
                    'id': self.poll_1_choice_1.id,
                },
                {
                    'votes': self.poll_1_choice_2.votes, 
                    'description': self.poll_1_choice_2.description, 
                    'id': self.poll_1_choice_2.id,
                },
            ]
        }
        response = self.client.get(reverse('poll', args=(self.poll_1.id, )))
        json_returned = json.loads(response.content)
        self.assertEqual(json_returned, expected_output)

    def test_api_without_poll_id_returns_json_of_all_polls(self):
        expected_output = [
            {
                'id': self.poll_1.id,
                'question': self.poll_1.question,
                'choices': [
                    {
                        'votes': self.poll_1_choice_1.votes, 
                        'description': self.poll_1_choice_1.description, 
                        'id': self.poll_1_choice_1.id,
                    },
                    {
                        'votes': self.poll_1_choice_2.votes, 
                        'description': self.poll_1_choice_2.description, 
                        'id': self.poll_1_choice_2.id,
                    },
                ]
            }, 
            {
                'id': self.poll_2.id,
                'question': self.poll_2.question,
                'choices': [
                    {
                        'votes': self.poll_2_choice_1.votes, 
                        'description': self.poll_2_choice_1.description, 
                        'id': self.poll_2_choice_1.id,
                    },
                    {
                        'votes': self.poll_2_choice_2.votes, 
                        'description': self.poll_2_choice_2.description, 
                        'id': self.poll_2_choice_2.id,
                    },
                ]
            }, 
        ]
        response = self.client.get(reverse('polls'))
        json_returned = json.loads(response.content)
        self.assertEqual(json_returned, expected_output)

    def test_should_add_vote_to_choice(self):
        choice = self.poll_2_choice_2

        self.assertEqual(0, self.poll_1_choice_2.votes)
        response = self.client.post(reverse('vote_poll'), {'choice': choice.id})
        
        choice = Choice.objects.get(pk=choice.id)  # Need to query again to check updated values
        self.assertEqual(1, choice.votes)


