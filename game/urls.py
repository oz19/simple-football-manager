from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (
    StartView,
    RouterView,
    ChallengeSelectionView,
    PreseasonView,
    FirstGamesView,
)


urlpatterns = [
    # Router (redirects to correct stage)
    path('', RouterView.as_view(), name='router'),

    # Game stages
    path(
        'start/',
        login_required(StartView.as_view()),
        name='home'
    ),
    path(
        'challenge-selection/',
        login_required(ChallengeSelectionView.as_view()),
        name='challenge_selection'
    ),
    path(
        'preseason/',
        login_required(PreseasonView.as_view()),
        name='preseason'
    ),
    path(
        'first-games/',
        login_required(FirstGamesView.as_view()),
        name='first-games'
    )
]
