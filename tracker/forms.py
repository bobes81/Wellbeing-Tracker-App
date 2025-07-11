from django import forms
from .models import MoodEntry, Workout

class MoodEntryForm(forms.ModelForm):
    class Meta:
        model = MoodEntry
        fields = ['mood', 'date', 'note']  # Added 'note'

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date', 'activity', 'duration', 'note']  # Added 'note'