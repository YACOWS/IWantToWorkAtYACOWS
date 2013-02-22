# -*- coding: utf-8 -*-
from django.test import TestCase

from ..models import Poll, Choice


class ChoiceTestCase(TestCase):

    def setUp(self):
        self.poll = Poll.objects.create(question="What's the answer to the Ultimate Question of Life, The Universe, and Everything?")

    def test_when_created_choice_must_have_no_votes(self):
        choice = Choice.objects.create(description='Test Choice', poll=self.poll)
        self.assertEqual(choice.votes, 0)

    def test_when_voted_increase_votes(self):
        choice = Choice.objects.create(description='Test Choice', poll=self.poll)

        choice.vote()
        self.assertEqual(choice.votes, 1)

        choice.vote()
        self.assertEqual(choice.votes, 2)
