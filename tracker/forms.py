from django import forms
from .models import Workout, Mood

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date', 'type', 'duration', 'notes']
        labels = {
            'date': 'Workout Date',
            'type': 'Workout Type',
            'duration': 'Duration (minutes)',
            'notes': 'Notes (optional)',
        }
        help_texts = {
            'duration': 'Enter duration between 1 and 600 minutes.',
        }

    def clean_duration(self):
        duration = self.cleaned_data['duration']
        if duration < 1 or duration > 600:
            raise forms.ValidationError('Duration must be between 1 and 600 minutes.')
        return duration


class MoodForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = ['mood_type', 'note']  # Exclude 'date'
        widgets = {
            'mood_type': forms.Select(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }