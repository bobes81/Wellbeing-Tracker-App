from django.contrib import admin
from .models import Workout, Mood  # Removed MoodEntry

admin.site.register(Workout)
admin.site.register(Mood)  # Register Mood instead of MoodEntry