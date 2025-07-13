from django.contrib import admin
from .models import Workout, Mood

@admin.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'mood_type', 'note')  # zobrazí správná pole v seznamu
    fields = ('user', 'mood_type', 'note')  # definuje, co se bude zobrazovat v detailu

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'type', 'duration')