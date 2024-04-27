import pytest
from rest_framework import status
from subscriptions.signals import calculate_subscription_end_date
from datetime import date

@pytest.mark.django_db
def test_create_payment(api_client, create_subscriber, pop_tables):
    url = "/subscription/payments/"
    subscriber = create_subscriber
    correct_payment_payload = {
        "method": "MasterCard",
        "card_name": "John Smith",
        "card_number": "0123456789012345",
        "amount": subscriber.subscription_plan.cost,
        "ends_in": "2026-10-01",
        "subscriber": subscriber.id,
    }
    response = api_client.post(url, correct_payment_payload)
    assert response.status_code == status.HTTP_201_CREATED
    
@pytest.mark.django_db
def test_create_payment_fails_card_number_invalid(api_client, create_subscriber, pop_tables):
    url = "/subscription/payments/"
    subscriber = create_subscriber
    correct_payment_payload = {
        "method": "MasterCard",
        "card_name": "John Smith",
        "card_number": "123456", # Invalid card number 
        "amount": subscriber.subscription_plan.cost,
        "ends_in": "2026-10-01",
        "subscriber": subscriber.id,
    }
    response = api_client.post(url, correct_payment_payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_create_payment_fails_missing_required_field(api_client, create_subscriber, pop_tables):
    url = "/subscription/payments/"
    subscriber = create_subscriber
    correct_payment_payload = {
        "method": "MasterCard",
        "card_name": "John Smith",
        "card_number": "0123456789012345",
        "ends_in": "2026-10-01",
        # Missing amount
        "subscriber": subscriber.id,
    }
    
    response = api_client.post(url, correct_payment_payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST    
    
@pytest.mark.django_db
def test_create_payment_fails_invalid_ends_in_date(api_client, create_subscriber, pop_tables):
    url = "/subscription/payments/"
    subscriber = create_subscriber
    correct_payment_payload = {
        "method": "MasterCard",
        "card_name": "John Smith",
        "card_number": "0123456789012345",
        "amount": subscriber.subscription_plan.cost,
        "ends_in": "2024-02-01", # Date is in the past
        "subscriber": subscriber.id,
    }
    response = api_client.post(url, correct_payment_payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_subscription_start_and_end_dates_set_when_payment_sucessful(api_client, create_subscriber, pop_tables):
    url = "/subscription/payments/"
    subscriber = create_subscriber
    correct_payment_payload = {
        "method": "MasterCard",
        "card_name": "John Smith",
        "card_number": "0123456789012345",
        "ends_in": "2026-10-01",
        "amount": subscriber.subscription_plan.cost,
        "subscriber": subscriber.id,
    }
    
    response = api_client.post(url, correct_payment_payload)
    subscriber.refresh_from_db()
    assert response.status_code == status.HTTP_201_CREATED
    assert subscriber.subscription_start_date == date.today()
    assert subscriber.subscription_end_date == calculate_subscription_end_date(subscriber)