from rest_framework import serializers
from .models import *

class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ['id', 'period', 'semesters', 'cost']
        
        
class PaymentSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        return super().validate(attrs)
    
    class Meta:
        model = Payment
        fields = ['id', 'method', 'card_name', 'card_number', 'ends_in', 'amount', 'subscriber']
        

