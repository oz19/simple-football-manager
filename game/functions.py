from django.core.validators import MaxValueValidator, MinValueValidator

from .models import (
    Challenge,
    Budget,
    PurposedChallenge
)

import random


def get_or_create_challenge_offers(user):
    '''Creates 3 challenge offers based on user's reputation

        Input: user (CustomUser instance)
        Output: 3 selectable options for radio buttons rendering (List)
    '''
    offers = []

    # Get purposed challenges (if any)
    purposed_challenges = PurposedChallenge.objects.filter(user=user)
    if len(purposed_challenges) == 3:
        for pc in purposed_challenges:
            offers.append(
                (
                    pc.challenge.id,
                    'Budget: %s € / Target pos.: %s/20 (Difficulty: %s/10)' %(
                        pc.challenge.budget.season_budget,
                        pc.challenge.target,
                        pc.challenge.difficulty
                    )
                )
            )
        return offers

    # Delete if any and purpose 3 new challenges if they don't exist
    purposed_challenges.delete()
    for _ in range(3):
        # Calculate variables
        target          = 1 + round(16 * random.random())
        season_budget   = calculate_season_budget(user.reputation)
        difficulty      = calculate_difficulty(target, season_budget, user.reputation)

        # Create instances
        budget = Budget.objects.create(season_budget=season_budget) # A signal will fill 'cash'
        challenge = Challenge.objects.create(
            budget      = budget,
            difficulty  = difficulty,
            target      = target
        )
        purposed_challenge = PurposedChallenge.objects.create(
            challenge=challenge,
            user=user
        )

        # Format data
        offers.append(
            (
                challenge.id,
                'Budget: %s € / Target pos.: %s/20 (Difficulty: %s/10)' %(
                    challenge.budget.season_budget,
                    challenge.target,
                    challenge.difficulty
                )
            )
        )
    return offers

def calculate_difficulty(target, season_budget, reputation):
    '''Calculates challenge difficulty based on target and season budget

        Inputs: target (Int [1-17]), budget (Int[0-1000000000])
    '''
    MIN_SEASON_BUDGET, MAX_SEASON_BUDGET = get_season_budget_limits()
    if reputation == 0: reputation = 1
    budget_variability_range    = (MAX_SEASON_BUDGET/100) * reputation # It is also aprox_budget
    min_budget_from_reputation  = budget_variability_range * 0.5
    max_budget_from_reputation  = budget_variability_range * 1.5

    # Calculate
    budget_evaluation       = 1 - ( (season_budget-min_budget_from_reputation) / budget_variability_range ) # 0:easy 1:difficult
    target_evaluation       = 1 - ( (target-1) / 16) # 0:easy 1:difficult
    target_budget_balance   = 0.5 * (budget_evaluation + target_evaluation)
    difficulty              = round(10 * target_budget_balance)

    if difficulty < 0: difficulty = 0
    elif difficulty > 10: difficulty = 10

    return difficulty
        

def calculate_season_budget(reputation):
    '''Calculates realistic season budgets for offers based on user's reputation

        Input   : reputation (Integer [0-100])
        Output  : budget (Integer [0-1000000000])
    '''
    # Get season_budget limits
    MIN_SEASON_BUDGET, MAX_SEASON_BUDGET = get_season_budget_limits()

    # Calculate season budget
    aprox_range = (MAX_SEASON_BUDGET/100) * reputation
    if aprox_range == 0:
        variability = int((MAX_SEASON_BUDGET/100) * random.random())
    else:
        variability = int(aprox_range * random.random())
    season_budget = round( int(aprox_range/2) + variability, -6)

    # Check limits
    if season_budget < MIN_SEASON_BUDGET:
        season_budget = MIN_SEASON_BUDGET
    elif season_budget > MAX_SEASON_BUDGET:
        season_budget = MAX_SEASON_BUDGET

    return season_budget

def get_season_budget_limits():
    '''Get season budget limits from model definition

        Input   : -
        Output  : min_limit, max_limit (Int [0-1000000000])
    '''
    min_limit = max_limit = None
    validators = Budget._meta.get_field('season_budget').validators

    for validator in validators:
        if isinstance(validator, MaxValueValidator):
            max_limit = validator.limit_value
        elif isinstance(validator, MinValueValidator):
            min_limit = validator.limit_value

    if not min_limit:
        min_limit = 0
    if not max_limit:
        max_limit = 1000000000

    return min_limit, max_limit
