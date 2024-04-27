from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PaymentViewSet, SubscriptionPlansView

router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns = [
    path('plans/', SubscriptionPlansView.as_view(), name='subscription-plans'),
    ] + router.urls