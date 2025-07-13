from django.contrib import admin
from .models import Workout, Mood

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'type', 'duration')

class MoodAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'mood_level', 'notes')

admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Mood, MoodAdmin)

