from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import (CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin)

from .models import *
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class EducationOptionsView(APIView):
    @swagger_auto_schema(
        operation_id="Get all options needed for subscription form",
        operation_description="Endpoint to get all education options needed for a subscription form.",
        responses={
            200: openapi.Response(
                'OK',
            ),
        },
    )
    def get(self, request):
        # All options needed for form
        education_levels = EducationLevel.objects.all()
        class_years = ClassYear.objects.all()
        cirriculums = Cirriculum.objects.all()
        subjects = Subject.objects.all()
        student_counts = StudentCount.objects.all()
        academic_goals = AcademicGoal.objects.all()
        suitable_days = SuitableDay.objects.all()
        suitable_day_periods = SuitableDayPeriod.objects.all()
        suitable_day_times = SuitableDayTime.objects.all()
        weekly_class_counts = WeeklyClassCount.objects.all()
        class_times = ClassTime.objects.all()
        
        # Serializers
        response_data = {}
        response_data['education_levels'] = EducationLevelSerializer(education_levels, many=True).data
        response_data['class_years'] = ClassYearSerializer(class_years, many=True).data
        response_data['cirriculums'] = CirriculumSerializer(cirriculums, many=True).data
        response_data['subjects'] = SubjectSerializer(subjects, many=True).data
        response_data['student_counts'] = StudentCountSerializer(student_counts, many=True).data
        response_data['academic_goals'] = AcademicGoalSerializer(academic_goals, many=True).data
        response_data['suitable_days'] = SuitableDaySerializer(suitable_days, many=True).data
        response_data['suitable_day_periods'] = SuitableDayPeriodSerializer(suitable_day_periods, many=True).data
        response_data['suitable_day_times'] = SuitableDayTimeSerializer(suitable_day_times, many=True).data
        response_data['weekly_class_counts'] = WeeklyClassCountSerializer(weekly_class_counts, many=True).data
        response_data['class_times'] = ClassTimeSerializer(class_times, many=True).data
        
        return Response(response_data, status=200)


