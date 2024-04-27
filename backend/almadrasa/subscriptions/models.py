from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator

def validate_future_date(value):
    """Validator that checks if the given date is in the future."""
    from django.core.exceptions import ValidationError
    from django.utils.timezone import now

    if value < now().date():
        raise ValidationError(_('Date cannot be in the past'))

    return value

class SubscriptionPlan(models.Model):
    period = models.IntegerField()
    semesters = models.IntegerField()
    cost = models.IntegerField()
    discount_applied = models.BooleanField(default=False)
    
    @property
    def discounted_cost(self):
        return (self.semesters * 0.05) * self.cost 
    
    def __str__(self) -> str:
        return str(str(self.period) +
                   _(" Months") + 
                   " - " + str(self.semesters) + 
                   _(" Semesters") + " - " +
                   str(self.cost) + " " + _("AED") +
                   " - " + "Discounted: " + str(self.discount_applied)
                   )
    
    class Meta:
        verbose_name = _("Subscription Plan")
        verbose_name_plural = _("Subscription Plans")

# NOTE: This model is simplified and for demonstration purposes only, 
# a payment gateway like PayPal or Stripe should be integrated for a production level system.
class Payment(models.Model):
    method = models.CharField(max_length=128)
    card_name = models.CharField(max_length=128)
    card_number = models.CharField(max_length=16, validators=[MinLengthValidator(16)])
    amount = models.FloatField()
    ends_in = models.DateField(validators=[validate_future_date])
    
    # TODO: Ideally, payment records should be preserved even if the subscriber 
    # is deleted. However, due to time constraints, on_delete=models.CASCADE 
    # is used for now. Consider implementing a default option to address this.
    subscriber = models.ForeignKey('users.Subscriber', on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")