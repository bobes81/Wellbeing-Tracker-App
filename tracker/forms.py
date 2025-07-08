from django import forms
from .models import Workout, MoodEntry

class WorkoutForm(forms.ModelForm):  # změněno z WorkoutEntryForm na WorkoutForm
    class Meta:
        model = Workout
        fields = ['title', 'date', 'duration', 'notes']

class MoodEntryForm(forms.ModelForm):
    class Meta:
        model = MoodEntry
        fields = ['date', 'mood', 'note']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'mood': forms.Select(),
            'note': forms.Textarea(attrs={'rows': 3}),
        }
