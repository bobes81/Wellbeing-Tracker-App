from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    WORKOUT_CHOICES = [
        ('Cardio', 'Cardio'),
        ('Strength', 'Strength'),
        ('Yoga', 'Yoga'),
        ('Stretching', 'Stretching'),
        ('Walking', 'Walking'),
        ('Cycling', 'Cycling'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    type = models.CharField(max_length=20, choices=WORKOUT_CHOICES)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.type}"
