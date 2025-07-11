from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")
    notes = models.TextField(blank=True, null=True)  # Existing field
    note = models.TextField(blank=True)  # <-- Added this field

    def __str__(self):
        return f"{self.title} on {self.date}"


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
    note = models.TextField(blank=True, null=True)  # Existing field
    note = models.TextField(blank=True)  # <-- Added this field

    class Meta:
        verbose_name = "Mood Log"
        verbose_name_plural = "Mood Logs"

    def __str__(self):
        return f"Mood on {self.date}: {self.mood}"
