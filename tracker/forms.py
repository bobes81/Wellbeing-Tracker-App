from django import forms
from .models import WorkoutEntry, MoodEntry

class WorkoutEntryForm(forms.ModelForm):
    class Meta:
        model = WorkoutEntry
        fields = ['date', 'workout_type', 'duration_minutes', 'intensity', 'bmi']

class MoodEntryForm(forms.ModelForm):
    class Meta:
        model = MoodEntry
        fields = ['date', 'mood', 'note']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'mood': forms.Select(),
            'note': forms.Textarea(attrs={'rows': 3}),
        }
