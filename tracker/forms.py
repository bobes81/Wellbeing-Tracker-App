from django import forms
from .models import Mood, Workout

class MoodForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = ['mood_level', 'notes']  # ❗️NEZAHRNUJ 'date'
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date', 'activity', 'duration', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }