import pytest
from rest_framework.test import APIClient
from education.models import (
    EducationLevel,
    ClassYear,
    Cirriculum,
    Subject,
    StudentCount,
    AcademicGoal,
    SuitableDay,
    SuitableDayPeriod,
    SuitableDayTime,
    WeeklyClassCount,
    ClassTime
)
from subscriptions.models import SubscriptionPlan
from users.models import Subscriber
import random
from education.utils import *


@pytest.fixture()
def api_client():
    return APIClient()

@pytest.fixture()
def admin_user(django_user_model):
    return django_user_model.objects.create_superuser(
        username="admin",
        password="123",
        email="admin@gmail.com",
        first_name="admin",
        last_name="admin",
    )

@pytest.fixture()
def pop_tables():
    EducationLevel.objects.bulk_create([EducationLevel(level=name) for name in education_levels])
    ClassYear.objects.bulk_create([ClassYear(year=name) for name in class_years])
    Cirriculum.objects.bulk_create([Cirriculum(cirriculum=name) for name in cirriculums])
    Subject.objects.bulk_create([Subject(subject=name) for name in subjects])
    StudentCount.objects.bulk_create([StudentCount(student_count=count) for count in student_counts])
    AcademicGoal.objects.bulk_create([AcademicGoal(goal=goal) for goal in academic_goals])
    SuitableDay.objects.bulk_create([SuitableDay(day=day) for day in suitable_days])
    SuitableDayPeriod.objects.bulk_create([SuitableDayPeriod(period=period) for period in suitable_day_period])
    SuitableDayTime.objects.bulk_create([SuitableDayTime(time=time) for time in suitable_day_time])
    WeeklyClassCount.objects.bulk_create([WeeklyClassCount(weekly_count=name) for name in weekly_class_count])
    ClassTime.objects.bulk_create([ClassTime(class_time=name) for name in class_time])
    SubscriptionPlan.objects.bulk_create([SubscriptionPlan(**plan) for plan in subscription_plans])

@pytest.fixture()
def create_subscriber(admin_user, pop_tables):
    valid_subscriber_data = {
        "first_name": "first",
        "last_name": "last",
        "email": "test_mail@gmail.com",
        "age": 20,
        "gender": "Male",
        "nationality": "Egyptian",
        "whatsapp": "01102851831",
        "difficulties": "True",
        "notes": "test notes",
        "education_level": random.choice(EducationLevel.objects.all()),
        "class_year": random.choice(ClassYear.objects.all()),
        "cirriculum": random.choice(Cirriculum.objects.all()),
        "student_count": random.choice(StudentCount.objects.all()),
        "suitable_day_periods": random.choice(SuitableDayPeriod.objects.all()),
        "suitable_day_times": random.choice(SuitableDayTime.objects.all()),
        "weekly_class_count": random.choice(WeeklyClassCount.objects.all()),
        "class_time": random.choice(ClassTime.objects.all()),
        "subscription_plan": random.choice(SubscriptionPlan.objects.all()),
    }
    subscriber = Subscriber.objects.create(**valid_subscriber_data)
    subscriber.subjects.set([random.choice(Subject.objects.all())])
    subscriber.academic_goals.set([random.choice(AcademicGoal.objects.all())])
    subscriber.suitable_days.set([random.choice(SuitableDay.objects.all())])
    
    return subscriber