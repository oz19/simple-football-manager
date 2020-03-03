from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (
    HomeView,
    RouterView,
    ChallengeSelectionView,
)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('router/', RouterView.as_view(), name='router'),

    # Game stages
    path(
        'challenge-selection/',
        login_required(ChallengeSelectionView.as_view()),
        name='challenge_selection'
    ),
]
