from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username


class ExerciseLog(models.Model):
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, default=1)
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255)
    exercise_type = models.CharField(max_length=100)
    exercise_duration = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.timestamp}"
