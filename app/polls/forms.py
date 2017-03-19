from django import forms

class PollVoteForm(forms.Form):
    vote = forms.ChoiceField(widget=forms.RadioSelect())
    
    def __init__(self, poll):
        forms.Form.__init__(self)
        self.fields['vote'].choices = [(choice.id, choice.choice) for choice in poll.choice_set.all()]
        
    