# -*- coding: utf-8 -*-
from django import forms

from .models import Choice


class PollVoteForm(forms.Form):
    choices = forms.ModelChoiceField(queryset=Choice.objects.none(), required=True, 
        widget=forms.RadioSelect, empty_label=None)

    def __init__(self, poll_id=None, *args, **kwargs):
        super(PollVoteForm, self).__init__(*args, **kwargs)
        self.fields['choices'].queryset = Choice.objects.filter(poll__id=poll_id)
