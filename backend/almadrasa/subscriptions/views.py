from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import (CreateModelMixin,
                                   ListModelMixin,
                                   RetrieveModelMixin,
                                   UpdateModelMixin,
                                   DestroyModelMixin,)
from .models import Payment, SubscriptionPlan
from .serializers import PaymentSerializer, SubscriptionPlanSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class PaymentViewSet(CreateModelMixin,
                     ListModelMixin,
                     RetrieveModelMixin,
                     GenericViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
    @swagger_auto_schema(
        operation_id="PaymentViewSet - Create",
        operation_description="Endpoint to create a payment.",
        responses={
            200: openapi.Response(
                'OK',
                PaymentSerializer(many=True)
            ),
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
class SubscriptionPlansView(APIView):

    @swagger_auto_schema(
        operation_id="SubscriptionPlansView - Get",
        operation_description="Endpoint to get all subscription plans.",
        responses={
            200: openapi.Response(
                'OK',
                SubscriptionPlanSerializer(many=True)
            ),
        },
    )
    def get(self, request):
        plans = SubscriptionPlan.objects.all()
        serializer = SubscriptionPlanSerializer(plans, many=True)
        return Response(serializer.data)