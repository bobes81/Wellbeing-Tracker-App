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
    date = models.DateField(auto_now_add=True)
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    note = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Mood Log"
        verbose_name_plural = "Mood Logs"

    def __str__(self):
        return f"{self.date} - {self.mood}"
