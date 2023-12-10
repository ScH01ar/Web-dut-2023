# admin.py

from django.contrib import admin
from .models import UserProfile, ExerciseLog


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'age', 'gender', 'class_name')

    def get_username(self, obj):
        return obj.get_username()


@admin.register(ExerciseLog)
class ExerciseLogAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'timestamp', 'location',
                    'exercise_type', 'exercise_duration', 'date')

    def get_username(self, obj):
        return obj.user_profile.get_username()
