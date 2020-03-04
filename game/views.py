from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    TemplateView,
    RedirectView,
    FormView,
)

from .forms import (
    ChallengeSelectionForm,
)
from .functions import get_or_create_challenge_offers
from .models import Challenge


class StartView(TemplateView):
    template_name = 'start.html'


class RouterView(RedirectView):

    stage_url_name = {
        0: 'challenge_selection',
        1: 'preseason',
    }

    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            try:
                challenge = Challenge.objects.get(user=user)
            except ObjectDoesNotExist:
                # No challenge assigned. Start game.
                return reverse('home')

            # Select stage and redirect
            if challenge.stage == 0:
                return reverse('preseason')

        return reverse('account_login')


class ChallengeSelectionView(FormView):
    template_name   = 'challenge-selection.html'
    form_class      = ChallengeSelectionForm
    success_url     = reverse_lazy('preseason')

    def get_form_kwargs(self):
        kwargs = super(ChallengeSelectionView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        data            = form.cleaned_data
        challenge_id    = int(data['challenge'])
        challenge       = Challenge.objects.get(id=challenge_id)

        challenge.user  = self.request.user
        challenge.save() 

        return super(ChallengeSelectionView, self).form_valid(form)


class PreseasonView(TemplateView):
    template_name   = 'preseason.html'
