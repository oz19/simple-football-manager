from django import forms

from .functions import get_or_create_challenge_offers
from .models import Budget


class ChallengeSelectionForm(forms.Form):

    def __init__(self, *args, **kwargs):
    
        # We need to pop it out kwargs before loading real fields
        self.user = kwargs.pop('user')

        super(ChallengeSelectionForm, self).__init__(*args, **kwargs)
        self.fields['challenge'] = forms.ChoiceField(
            choices     = get_or_create_challenge_offers(user=self.user),
            widget      = forms.RadioSelect
        )

class PreseasonForm(forms.ModelForm):

    class Meta:
        model   = Budget
        fields  = [
            'players', 'facilities'
        ]
