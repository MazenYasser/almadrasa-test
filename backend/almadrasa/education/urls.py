from django.urls import path
from .views import EducationOptionsView

urlpatterns = [
    path('subscription-form/', EducationOptionsView.as_view(), name='subscription-form'),
]