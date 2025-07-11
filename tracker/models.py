from django.db import models
from django.contrib.auth.models import User

class MoodEntry(models.Model):
    MOOD_CHOICES = [
        ('Happy', 'Happy'),
        ('Neutral', 'Neutral'),
        ('Sad', 'Sad'),
        ('Anxious', 'Anxious'),
        ('Angry', 'Angry'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    mood = models.CharField(max_length=50, choices=MOOD_CHOICES)
    note = models.TextField(blank=True, null=True)  # Added note field

    def __str__(self):
        return f"Mood on {self.date}: {self.mood}"


class Workout(models.Model):
    activity = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in minutes")
    date = models.DateField()
    note = models.TextField(blank=True, null=True)  # Added note field

    def __str__(self):
        return f"{self.activity} on {self.date}"
