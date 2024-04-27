import pytest
import random
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
from rest_framework import status


# Changing to Arabic data later if time allows
@pytest.mark.django_db
def test_create_subscriber_with_correct_payload(api_client, admin_user, pop_tables):
    url = "/user/subscribers/"
    correct_subscriber_payload = {
        "first_name": "first",
        "last_name": "last",
        "email": "test_mail@gmail.com",
        "age": 20,
        "gender": "Male",
        "nationality": "Egyptian",
        "whatsapp": "01102851831",
        "difficulties": "True",
        "notes": "test notes",
        "education_level": random.choice(EducationLevel.objects.all()).id,
        "class_year": random.choice(ClassYear.objects.all()).id,
        "cirriculum": random.choice(Cirriculum.objects.all()).id,
        "subjects": [random.choice(Subject.objects.all()).id],
        "student_count": random.choice(StudentCount.objects.all()).id,
        "academic_goals": [random.choice(AcademicGoal.objects.all()).id],
        "suitable_days": [random.choice(SuitableDay.objects.all()).id],
        "suitable_day_periods": random.choice(SuitableDayPeriod.objects.all()).id,
        "suitable_day_times": random.choice(SuitableDayTime.objects.all()).id,
        "weekly_class_count": random.choice(WeeklyClassCount.objects.all()).id,
        "class_time": random.choice(ClassTime.objects.all()).id,
        
        # Should we set a subscription plan before a payment is made?
        "subscription_plan": random.choice(SubscriptionPlan.objects.all()).id,
    }

    response = api_client.post(url, correct_subscriber_payload, format='json')
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_create_subscriber_fails_missing_required_field(api_client, admin_user, pop_tables):
    url = "/user/subscribers/"
    incorrect_payload = { 
        # Missing first_name
        "last_name": "last",
        "email": "test_mail@gmail.com",
        "age": 20,
        "gender": "Male",
        "nationality": "Egyptian",
        "whatsapp": "01102851831",
        "difficulties": "True",
        "notes": "test notes",
        "education_level": random.choice(EducationLevel.objects.all()).id,
        "class_year": random.choice(ClassYear.objects.all()).id,
        "cirriculum": random.choice(Cirriculum.objects.all()).id,
        "subjects": [random.choice(Subject.objects.all()).id],
        "student_count": random.choice(StudentCount.objects.all()).id,
        "academic_goals": [random.choice(AcademicGoal.objects.all()).id],
        "suitable_days": [random.choice(SuitableDay.objects.all()).id],
        "suitable_day_periods": random.choice(SuitableDayPeriod.objects.all()).id,
        "suitable_day_times": [random.choice(SuitableDayTime.objects.all()).id],
        "weekly_class_count": random.choice(WeeklyClassCount.objects.all()).id,
        "class_time": random.choice(ClassTime.objects.all()).id,
        "subscription_plan": random.choice(SubscriptionPlan.objects.all()).id,
    }

    response = api_client.post(url, incorrect_payload, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_create_subscriber_invalid_field_value(api_client, admin_user, pop_tables):
    url = "/user/subscribers/"
    incorrect_payload = {
        "first_name": "first",
        "last_name": "last",
        "email": "invalid_email",  # Invalid email format
        "age": 20,
        "gender": "Male",
        "nationality": "Egyptian",
        "whatsapp": "01102851831",
        "difficulties": "True",
        "notes": "test notes",
        "education_level": random.choice(EducationLevel.objects.all()).id,
        "class_year": random.choice(ClassYear.objects.all()).id,
        "cirriculum": random.choice(Cirriculum.objects.all()).id,
        "subjects": [random.choice(Subject.objects.all()).id],
        "student_count": random.choice(StudentCount.objects.all()).id,
        "academic_goals": [random.choice(AcademicGoal.objects.all()).id],
        "suitable_days": [random.choice(SuitableDay.objects.all()).id],
        "suitable_day_periods": random.choice(SuitableDayPeriod.objects.all()).id,
        "suitable_day_times": [random.choice(SuitableDayTime.objects.all()).id],
        "weekly_class_count": random.choice(WeeklyClassCount.objects.all()).id,
        "class_time": random.choice(ClassTime.objects.all()).id,
        "subscription_plan": random.choice(SubscriptionPlan.objects.all()).id,
    }

    response = api_client.post(url, incorrect_payload, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_create_subscriber_fails_empty_required_field(api_client, admin_user, pop_tables):
    url = "/user/subscribers/"
    incorrect_payload = {
        "first_name": "test",
        "last_name": "last",
        "email": "test_mail@gmail.com",
        "age": 20,
        "gender": "Male",
        "nationality": "", # Nationality is empty
        "whatsapp": "01102851831",
        "difficulties": "True",
        "notes": "test notes",
        "education_level": random.choice(EducationLevel.objects.all()).id,
        "class_year": random.choice(ClassYear.objects.all()).id,
        "cirriculum": random.choice(Cirriculum.objects.all()).id,
        "subjects": [random.choice(Subject.objects.all()).id],
        "student_count": random.choice(StudentCount.objects.all()).id,
        "academic_goals": [random.choice(AcademicGoal.objects.all()).id],
        "suitable_days": [random.choice(SuitableDay.objects.all()).id],
        "suitable_day_periods": random.choice(SuitableDayPeriod.objects.all()).id,
        "suitable_day_times": [random.choice(SuitableDayTime.objects.all()).id],
        "weekly_class_count": random.choice(WeeklyClassCount.objects.all()).id,
        "class_time": random.choice(ClassTime.objects.all()).id,
        "subscription_plan": random.choice(SubscriptionPlan.objects.all()).id,
    }

    response = api_client.post(url, incorrect_payload, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_create_subscriber_invalid_phone(api_client, admin_user, pop_tables):
    url = "/user/subscribers/"
    incorrect_payload = {
        "first_name": "test",
        "last_name": "last",
        "email": "test_mail@gmail.com",
        "age": 20,
        "gender": "Male",
        "nationality": "Egyptian",
        "whatsapp": "1234567891234689497896869658", # Phone number longer than expected
        "difficulties": "True",
        "notes": "test notes",
        "education_level": random.choice(EducationLevel.objects.all()).id,
        "class_year": random.choice(ClassYear.objects.all()).id,
        "cirriculum": random.choice(Cirriculum.objects.all()).id,
        "subjects": [random.choice(Subject.objects.all()).id],
        "student_count": random.choice(StudentCount.objects.all()).id,
        "academic_goals": [random.choice(AcademicGoal.objects.all()).id],
        "suitable_days": [random.choice(SuitableDay.objects.all()).id],
        "suitable_day_periods": random.choice(SuitableDayPeriod.objects.all()).id,
        "suitable_day_times": [random.choice(SuitableDayTime.objects.all()).id],
        "weekly_class_count": random.choice(WeeklyClassCount.objects.all()).id,
        "class_time": random.choice(ClassTime.objects.all()).id,
        "subscription_plan": random.choice(SubscriptionPlan.objects.all()).id,
    }

    response = api_client.post(url, incorrect_payload, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    incorrect_payload["whatsapp"] = "12345678" # Phone number shorter than expected
    response = api_client.post(url, incorrect_payload, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
