from django.test import TestCase

from .models import Challenge
from users.models import CustomUser


class ChallengeTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create()

    def test_create_new_challenge(self):
        challenge = Challenge.objects.create(user = self.user)
        self.assertEqual(challenge.target, 10)
        self.assertEqual(challenge.current_position, 10)
        self.assertEqual(challenge.score, 5)
        self.assertEqual(challenge.difficulty, 5)
        self.assertEqual(challenge.stage, 'PRE')
        self.assertIsInstance(self.user, CustomUser)

