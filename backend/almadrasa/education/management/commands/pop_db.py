from django.core.management.base import BaseCommand
from users.models import *
from subscriptions.models import SubscriptionPlan
from education.models import *
from django.db import transaction

# Dummy data for each model to populate database
# Data was added by hand because the sample size is small, larger sample sizes would be automatically generated

education_levels = ['رياض الأطفال', 'التعليم الابتدائي', 'التعليم الإعدادي', 'التعليم الثانوي']
class_years = ['الصف الأول', 'الصف الثاني', 'الصف الثالث', 'الصف الرابع']
cirriculums = ['أمريكي', 'بريطاني', 'وزاري', 'أخرى']

# TODO: Import images for these subjects automatically, Import by hand for now
subjects = ['اللغة الإنجليزية', 'الرياضيات','الفيزياء','الأحياء','اللغة الألمانية','اللغة الفرنسية','اللغة العربية','الكيمياء', 'الكمبيوتر']
student_counts = ['طالب', 'طالبان', 'ثلاثة طلاب', 'أكثر من ذلك']
academic_goals = ['زيادة الدرجات', 'التحضير للامتحانات', 'حل  الواجب', 'أخرى']
suitable_days = ['السبت', 'الأحد', 'الإثنين', 'الثلاثاء', 'الاربعاء', 'الخميس', 'الجمعة']
suitable_day_period = ['وقت الصباح', 'وقت المساء']
suitable_day_time = ['10:00', '12:00', '14:00']
weekly_class_count = ['حصة واحدة', 'حصتين']
class_time = ['30 دقيقة', 'ساعة واحدة', 'ساعة و نصف', 'ساعتان', 'ساعتان و نصف']
subscription_plans = [{"period": 3, "semesters": 1, "cost": 100, "discount_applied": False},
                                            {"period": 6, "semesters": 2, "cost": 200, "discount_applied": False},
                                            {"period": 12, "semesters": 3, "cost": 300, "discount_applied": True}]


class Command(BaseCommand):
    help = "Reset and populate the DB with predetermined data"
    
    @transaction.atomic
    def handle(self, *args, **kwargs):
        # Remove existing users
        Subscriber.objects.all().delete()
        
        # Removing all existing data
        EducationLevel.objects.all().delete()
        ClassYear.objects.all().delete()
        Cirriculum.objects.all().delete()
        Subject.objects.all().delete()
        StudentCount.objects.all().delete()
        AcademicGoal.objects.all().delete()
        SuitableDay.objects.all().delete()
        SuitableDayPeriod.objects.all().delete()
        SuitableDayTime.objects.all().delete()
        WeeklyClassCount.objects.all().delete()
        ClassTime.objects.all().delete()
        SubscriptionPlan.objects.all().delete()
        
        # Populating the database
        EducationLevel.objects.bulk_create([EducationLevel(level=name) for name in education_levels])
        ClassYear.objects.bulk_create([ClassYear(year=name) for name in class_years])
        Cirriculum.objects.bulk_create([Cirriculum(cirriculum=name) for name in cirriculums])
        Subject.objects.bulk_create([Subject(subject=name) for name in subjects])
        StudentCount.objects.bulk_create([StudentCount(student_count=count) for count in student_counts])
        AcademicGoal.objects.bulk_create([AcademicGoal(goal=goal) for goal in academic_goals])
        SuitableDay.objects.bulk_create([SuitableDay(day=day) for day in suitable_days])
        SuitableDayPeriod.objects.bulk_create([SuitableDayPeriod(period=period) for period in suitable_day_period])
        SuitableDayTime.objects.bulk_create([SuitableDayTime(time=time) for time in suitable_day_time])
        WeeklyClassCount.objects.bulk_create([WeeklyClassCount(weekly_count=name) for name in weekly_class_count])
        ClassTime.objects.bulk_create([ClassTime(class_time=name) for name in class_time])
        SubscriptionPlan.objects.bulk_create([SubscriptionPlan(**plan) for plan in subscription_plans])
        
        
        self.stdout.write(self.style.SUCCESS('Successfully populated the database.'))

