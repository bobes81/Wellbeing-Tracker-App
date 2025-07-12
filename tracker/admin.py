from django.contrib import admin
from .models import Workout, Mood  # Ensure both models are defined in models.py

admin.site.register(Workout)
admin.site.register(Mood)