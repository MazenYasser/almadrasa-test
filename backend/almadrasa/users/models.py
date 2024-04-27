import datetime
from enum import Enum
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from education.models import *
from subscriptions.models import SubscriptionPlan
from django.utils import timezone
from django.db import transaction
from django.core.validators import RegexValidator, MaxValueValidator

phone_number_validator = RegexValidator(
    regex=r'^(\+?\d{10,18})$',
    message=_(
        'Invalid phone number. Phone number may or may not start with "+". Minimum length of 10 numbers. Max length of 18 numbers. Only numbers and "+" are allowed.'
    )
)





class User(AbstractUser):
    pass

class GenderChoices(Enum):
    MALE = _("Male")
    FEMALE = _("Female")


class Subscriber(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    age = models.IntegerField(validators=[MaxValueValidator(100)])
    gender = models.CharField(max_length=5, choices=[
                             (choice.value, choice.value) for choice in GenderChoices])
    nationality = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=15, validators=[phone_number_validator])
    difficulties = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)
    
    # Education Relations
    education_level = models.ForeignKey(EducationLevel, on_delete=models.PROTECT)
    class_year = models.ForeignKey(ClassYear, on_delete=models.PROTECT)
    cirriculum = models.ForeignKey(Cirriculum, on_delete=models.PROTECT)
    subjects = models.ManyToManyField(Subject)
    student_count = models.ForeignKey(StudentCount, on_delete=models.PROTECT)
    academic_goals = models.ManyToManyField(AcademicGoal)
    suitable_days = models.ManyToManyField(SuitableDay)
    suitable_day_periods = models.ForeignKey(SuitableDayPeriod, on_delete=models.PROTECT)
    suitable_day_times = models.ForeignKey(SuitableDayTime, on_delete=models.PROTECT)
    weekly_class_count = models.ForeignKey(WeeklyClassCount, on_delete=models.PROTECT)
    class_time = models.ForeignKey(ClassTime, on_delete=models.PROTECT)
    
    # Subscription Relations
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.PROTECT)
    join_date = models.DateField(auto_now_add=True)
    subscription_start_date = models.DateField(null=True, blank=True)
    subscription_end_date = models.DateField(null=True, blank=True)
    
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
