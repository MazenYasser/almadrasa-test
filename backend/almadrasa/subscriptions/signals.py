from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Payment
from django.utils import timezone

def calculate_subscription_end_date(subscriber):
        """ Calculates the subscription end date 
            based on the subscription plan period and the current time.

        Returns:
            Subscription end date -> datetime.date
        """
        # Get current date with timezone awareness
        now = date.today()
        
        # Add the subscription period from the plan
        return now + timezone.timedelta(days=(subscriber.subscription_plan.period * 30))

@receiver(post_save, sender=Payment)
def update_subscription_date_on_payment(sender, instance, created, **kwargs):
    """
    Updates the subscription start and end dates for a subscriber when a payment instance is created. 

    Parameters:
        sender: The sender of the signal.
        instance: The payment instance that triggered the signal.
        created: A boolean indicating if the instance was created.
        **kwargs: Additional keyword arguments.

    Returns:
        None
    """
    if created:
        subscriber = instance.subscriber
        subscriber.subscription_start_date = date.today()
        subscriber.subscription_end_date = calculate_subscription_end_date(subscriber)
        subscriber.save()