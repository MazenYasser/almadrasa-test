from django.contrib import admin
from .models import (
    EducationLevel,
    ClassYear,
    Cirriculum,
    Subject,
    StudentCount,
    AcademicGoal,
    SuitableDay,
    SuitableDayPeriod,
    SuitableDayTime,
    WeeklyClassCount,
    ClassTime,
)

admin.site.register(EducationLevel)
admin.site.register(ClassYear)
admin.site.register(Cirriculum)
admin.site.register(Subject)
admin.site.register(StudentCount)
admin.site.register(AcademicGoal)
admin.site.register(SuitableDay)
admin.site.register(SuitableDayPeriod)
admin.site.register(SuitableDayTime)
admin.site.register(WeeklyClassCount)
admin.site.register(ClassTime)
