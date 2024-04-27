from os import set_inheritable
from rest_framework import serializers
from .models import *
from education.serializers import *
from subscriptions.serializers import *

class SubscriberReadSerializer(serializers.ModelSerializer):
    education_level = EducationLevelSerializer()
    class_year = ClassYearSerializer()
    cirriculum = CirriculumSerializer()
    subjects = SubjectSerializer(many=True)
    student_count = StudentCountSerializer()
    academic_goals = AcademicGoalSerializer(many=True)
    suitable_days = SuitableDaySerializer(many=True)
    suitable_day_periods = SuitableDayPeriodSerializer()
    suitable_day_times = SuitableDayTimeSerializer()
    weekly_class_count = WeeklyClassCountSerializer()
    class_time = ClassTimeSerializer()
    subscription_plan = SubscriptionPlanSerializer()
    
    class Meta:
        model = Subscriber
        fields = [
            'first_name',
            'last_name',
            'email',
            'age',
            'gender',
            'nationality',
            'whatsapp',
            'difficulties',
            'notes',
            
            'education_level',
            'class_year',
            'cirriculum',
            'subjects',
            'student_count',
            'academic_goals',
            'suitable_days',
            'suitable_day_periods',
            'suitable_day_times',
            'weekly_class_count',
            'class_time',
            'subscription_plan',
            'subscription_start_date',
            'subscription_end_date',
            ]

class SubscriberWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriber
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'age',
            'gender',
            'nationality',
            'whatsapp',
            'difficulties',
            'notes',
            
            'education_level',
            'class_year',
            'cirriculum',
            'subjects',
            'student_count',
            'academic_goals',
            'suitable_days',
            'suitable_day_periods',
            'suitable_day_times',
            'weekly_class_count',
            'class_time',
            'subscription_plan',
            'subscription_start_date',
            'subscription_end_date',
            ]