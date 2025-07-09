from django import forms
from .models import Workout, MoodEntry

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['title', 'date', 'duration', 'notes']

class MoodEntryForm(forms.ModelForm):
    class Meta:
        model = MoodEntry
        fields = ['date', 'mood', 'note']
# Trigger redeploy
