from enum import Enum
from django.db import models
from django.utils.translation import gettext_lazy as _

# ONE TO MANY
class EducationLevel(models.Model):
    level = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.level

    class Meta:
        verbose_name = _("Education Level")
        verbose_name_plural = _("Education Levels")

# ONE TO MANY
class ClassYear(models.Model):
    year = models.CharField(max_length=128)
    
    def __str__(self) -> str:
        return self.year

    class Meta:
        verbose_name = _("Class Year")
        verbose_name_plural = _("Class Years")

# ONE TO MANY
class Cirriculum(models.Model):
    cirriculum = models.CharField(max_length=128)

    def __str__(self):
        return self.cirriculum

    class Meta:
        verbose_name = _("Cirriculum")
        verbose_name_plural = _("Cirriculums")


# MANY TO MANY
class Subject(models.Model):
    subject = models.CharField(max_length=128)
    image = models.ImageField(upload_to="subjects/", null=True, blank=True, max_length=1024)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")


# ONE TO MANY
class StudentCount(models.Model):
    student_count = models.CharField(max_length=128)
    
    def __str__(self):
        return str(self.student_count)
    
    class Meta:
        verbose_name = _("Student Count")
        verbose_name_plural = _("Student Counts")

# MANY TO MANY
class AcademicGoal(models.Model):
    goal = models.CharField(max_length=128)
    
    def __str__(self) -> str:
        return self.goal
    
    class Meta:
        verbose_name = _("Academic Goal")
        verbose_name_plural = _("Academic Goals")
        

class SuitableDayChoices(Enum):
    SATURDAY = _("Saturday")
    SUNDAY = _("Sunday")
    MONDAY = _("Monday")
    TUESDAY = _("Tuesday")
    WEDNESDAY = _("Wednesday")
    THURSDAY = _("Thursday")
    FRIDAY = _("Friday")
    

# MANY TO MANY
class SuitableDay(models.Model):
    day = models.CharField(max_length=128, choices=[(day.value, day.value) for day in SuitableDayChoices])
    
    def __str__(self) -> str:
        return self.day
    
    class Meta:
        verbose_name = _("Suitable Day")
        verbose_name_plural = _("Suitable Days")

# ONE TO MANY
class SuitableDayPeriodChoices(Enum):
    MORNING_TIME = _("Morning time")
    EVENING_TIME = _("Evening time")

class SuitableDayPeriod(models.Model):
    period = models.CharField(max_length=128, choices=[(period.value, period.value) for period in SuitableDayPeriodChoices])
    
    def __str__(self) -> str:
        return self.period
    
    class Meta:
        verbose_name = _("Suitable Day Period")
        verbose_name_plural = _("Suitable Day Periods")


# ONE TO MANY
class SuitableDayTime(models.Model):
    time = models.TimeField()
    
    def __str__(self) -> str:
        return str(self.time)
    
    class Meta:
        verbose_name = _("Suitable Day Time")
        verbose_name_plural = _("Suitable Day Times")
        

# ONE TO MANY
class WeeklyClassCount(models.Model):
    weekly_count = models.CharField(max_length=128)
    
    def __str__(self) -> str:
        return self.weekly_count
    
    
    class Meta:
        verbose_name = _("Weekly Class")
        verbose_name_plural = _("Weekly Classes")
        
        
# ONE TO MANY
class ClassTime(models.Model):
    class_time = models.CharField(max_length=128)
    
    def __str__(self) -> str:
        return str(self.class_time)
    
    class Meta:
        verbose_name = _("Class Time")
        verbose_name_plural = _("Class Times")
        
