from django import forms
from .models import Workout, Mood

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date', 'type', 'duration', 'notes']

class MoodForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = ['date', 'mood_level', 'note']