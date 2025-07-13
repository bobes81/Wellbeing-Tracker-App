from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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
    type = models.CharField(max_length=100, default="Cardio")
    activity = models.CharField(max_length=100, default="")  # ⬅️ Added new field
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.type}"

MOOD_CHOICES = [
    (1, 'Very Low'),
    (2, 'Low'),
    (3, 'Neutral'),
    (4, 'Good'),
    (5, 'Very Good'),
]

class Mood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    mood_level = models.IntegerField(choices=MOOD_CHOICES, default=3)  # ✅ Default value set
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.get_mood_level_display()}"
