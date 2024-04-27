from rest_framework import serializers
from .models import *

class EducationLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = EducationLevel
        fields = ['id', 'level']

class ClassYearSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassYear
        fields = ['id', 'year']

class CirriculumSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cirriculum
        fields = ['id', 'cirriculum']
        
class SubjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image_url')
    
    # This is for local development environment purposes
    def get_image_url(self, subject):
        if subject.image:
            return "http://127.0.0.1:8000" + subject.image.url

    class Meta:
        model = Subject
        fields = ['id', 'subject', 'image']
        
class StudentCountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudentCount
        fields = ['id', 'student_count']
        
class AcademicGoalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AcademicGoal
        fields = ['id', 'goal']
        
class SuitableDaySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SuitableDay
        fields = ['id', 'day']
        
class SuitableDayPeriodSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SuitableDayPeriod
        fields = ['id', 'period']
        
class SuitableDayTimeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SuitableDayTime
        fields = ['id', 'time']

class WeeklyClassCountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WeeklyClassCount
        fields = ['id', 'weekly_count']

class ClassTimeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClassTime
        fields = ['id', 'class_time']


