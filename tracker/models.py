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
    type = models.CharField(max_length=100, default="Cardio")  # Updated max_length from 20 to 100
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.type}"

class Mood(models.Model):
    MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('neutral', 'Neutral'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
        ('tired', 'Tired'),
        ('motivated', 'Motivated'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    mood_type = models.CharField(max_length=20, choices=MOOD_CHOICES)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.get_mood_type_display()}"
