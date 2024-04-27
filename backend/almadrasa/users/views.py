from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import (CreateModelMixin,
                                   ListModelMixin,
                                   RetrieveModelMixin,
                                   UpdateModelMixin,
                                   DestroyModelMixin)
from .models import Subscriber
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class SubscriberViewSet(ModelViewSet):
    queryset = Subscriber.objects.all()
    
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return SubscriberReadSerializer
        else:
            return SubscriberWriteSerializer

    
    @swagger_auto_schema(
        operation_description="List all subscribers",
        responses={200: SubscriberReadSerializer(many=True)},
        tags=['Subscribers']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Retrieve a single subscriber",
        responses={200: SubscriberReadSerializer()},
        tags=['Subscribers']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Create a new subscriber",
        request_body=SubscriberWriteSerializer,
        responses={201: SubscriberReadSerializer()},
        tags=['Subscribers']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)