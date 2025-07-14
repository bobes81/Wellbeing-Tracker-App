from django import forms
from .models import Mood, Workout

class MoodForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = ['mood_level', 'notes']  # 👈 'date' zde nesmí být!
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date', 'type', 'activity', 'duration', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'type': forms.Select(),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }