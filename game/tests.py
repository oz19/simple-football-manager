from django.test import TestCase

from .models import Budget, Challenge
from users.models import CustomUser


class BudgetTests(TestCase):

    def setUp(self):
        self.budget = Budget.objects.create()

    def test_create_new_budget(self):
        self.assertEqual(self.budget.season_budget, 0)
        self.assertEqual(self.budget.cash, 0)
        self.assertEqual(self.budget.players, 0)
        self.assertEqual(self.budget.staff, 0)
        self.assertEqual(self.budget.bonus, 0)
        self.assertEqual(self.budget.marketing, 0)
        self.assertEqual(self.budget.team_building, 0)
        self.assertEqual(self.budget.education, 0)
        self.assertEqual(self.budget.facilities, 0)


class ChallengeTests(TestCase):

    def setUp(self):
        self.user       = CustomUser.objects.create(username = 'testuser')
        self.budget     = Budget.objects.create()
        self.challenge  = Challenge.objects.create(
            user    = self.user,
            budget  = self.budget
        )

    def test_create_new_challenge_with_user_and_budget(self):
        self.assertEqual(self.challenge.target, 10)
        self.assertEqual(self.challenge.current_position, 10)
        self.assertEqual(self.challenge.score, 5)
        self.assertEqual(self.challenge.difficulty, 5)
        self.assertEqual(self.challenge.stage, 'PRE')
        self.assertIsInstance(self.challenge.user, CustomUser)
        self.assertIsInstance(self.challenge.budget, Budget)

    def test_create_new_challenge_without_user_or_budget(self):
        self.challenge = Challenge.objects.create()
        self.assertEqual(self.challenge.target, 10)
        self.assertEqual(self.challenge.current_position, 10)
        self.assertEqual(self.challenge.score, 5)
        self.assertEqual(self.challenge.difficulty, 5)
        self.assertEqual(self.challenge.stage, 'PRE')
        self.assertNotIsInstance(self.challenge.user, CustomUser)
        self.assertNotIsInstance(self.challenge.budget, Budget)

    def test_create_new_challenge_with_user_without_budget(self):
        self.challenge = Challenge.objects.create(
            user = CustomUser.objects.create(username='testuser2')
        )
        self.assertEqual(self.challenge.target, 10)
        self.assertEqual(self.challenge.current_position, 10)
        self.assertEqual(self.challenge.score, 5)
        self.assertEqual(self.challenge.difficulty, 5)
        self.assertEqual(self.challenge.stage, 'PRE')
        self.assertIsInstance(self.challenge.user, CustomUser)
        self.assertNotIsInstance(self.challenge.budget, Budget)

    def test_create_new_challenge_with_budget_without_user(self):
        self.challenge = Challenge.objects.create(
            budget = Budget.objects.create()
        )
        self.assertEqual(self.challenge.target, 10)
        self.assertEqual(self.challenge.current_position, 10)
        self.assertEqual(self.challenge.score, 5)
        self.assertEqual(self.challenge.difficulty, 5)
        self.assertEqual(self.challenge.stage, 'PRE')
        self.assertNotIsInstance(self.challenge.user, CustomUser)
        self.assertIsInstance(self.challenge.budget, Budget)

