from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Budget


###############################################################################
#
# This signal is easily avoidable. It has been created just for showing how
# to set signals on Django.
# 
################################################################################

@receiver(post_save, sender=Budget)
def set_cash_on_budget_creation(sender, instance, created, **kwargs):
    if created:
        instance.cash = instance.season_budget
        instance.save()
