from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.views.generic import TemplateView, RedirectView

from .functions import create_challenge_offers
from .models import Challenge


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user and self.request.user.is_authenticated:
            try:
                context['challenge'] = Challenge.objects.get(user=self.request.user)
            except ObjectDoesNotExist:
                context['challenge'] = None
        return context


class RouterView(RedirectView):

    stage_url_name = {
        0: 'challenge_selection',
        1: 'preseason',
    }

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse('home')
        return reverse('account_login')


class ChallengeSelectionView(TemplateView):
    template_name   = 'challenge-selection.html'
