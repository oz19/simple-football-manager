from django import forms

from .functions import create_challenge_offers


class ChallengeSelectionForm(forms.Form):
    def __init__(self, reputation, *args, **kwargs):
        super(ChallengeSelectionForm, self).__init__(*args, **kwargs)
        challenge = forms.ChoiceField(
            choices = create_challenge_offers(reputation=20),
            widget  = forms.RadioSelect
        )
