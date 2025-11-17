from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView
from .models import Workout, Mood
from .forms import WorkoutForm, MoodForm
import logging

# -------------------------------
#              HOME
# -------------------------------

def home(request):
    """Render the homepage with the current timestamp."""
    return render(request, 'tracker/home.html', {'now': now()})

# -------------------------------
#           REGISTRATION
# -------------------------------

def register(request):
    """Register a new user and log them in automatically."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# -------------------------------
#            WORKOUTS
# -------------------------------

@login_required
def workout_list(request):
    """Display all workouts belonging to the logged-in user."""
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'tracker/workout_list.html', {'workouts': workouts})

@login_required
def add_workout(request):
    """Create a new workout record."""
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm()
    return render(request, 'tracker/workout_form.html', {'form': form})

@login_required
def edit_workout(request, pk):
    """Edit an existing workout."""
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'tracker/workout_form.html', {'form': form})

@login_required
def delete_workout(request, pk):
    """Delete a workout after user confirmation."""
    workout = get_object_or_404(Workout, pk=pk, user=request.user)

    if request.method == 'POST':
        workout.delete()
        return redirect('workout_list')

    # Render confirmation template
    return render(request, 'tracker/workout_confirm_delete.html', {'workout': workout})

# -------------------------------
#              MOODS
# -------------------------------

@login_required
def mood_list(request):
    """Display a list of all mood entries for the logged-in user."""
    try:
        moods = Mood.objects.filter(user=request.user).order_by('-date')
        return render(request, 'tracker/mood_list.html', {'moods': moods})
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error("Error in mood_list view: %s", str(e))
        raise

@login_required
def add_mood(request):
    """Create a new mood entry."""
    if request.method == 'POST':
        form = MoodForm(request.POST)
        if form.is_valid():
            mood = form.save(commit=False)
            mood.user = request.user
            mood.save()
            return redirect('mood_list')
    else:
        form = MoodForm()
    return render(request, 'tracker/mood_form.html', {'form': form})

@login_required
def edit_mood(request, pk):
    """Edit an existing mood entry."""
    mood = get_object_or_404(Mood, pk=pk, user=request.user)
    if request.method == 'POST':
        form = MoodForm(request.POST, instance=mood)
        if form.is_valid():
            form.save()
            return redirect('mood_list')
    else:
        form = MoodForm(instance=mood)
    return render(request, 'tracker/mood_form.html', {'form': form})

@login_required
def delete_mood(request, pk):
    """Delete a mood entry after confirmation."""
    mood = get_object_or_404(Mood, pk=pk, user=request.user)

    if request.method == 'POST':
        mood.delete()
        return redirect('mood_list')

    return render(request, 'tracker/mood_confirm_delete.html', {'mood': mood})

# -------------------------------
#        CLASS-BASED VIEW
# -------------------------------

class MoodListView(ListView):
    """Alternative class-based view for displaying mood entries."""
    model = Mood
    template_name = 'tracker/mood_list.html'
    context_object_name = 'moods'

    def get_queryset(self):
        return Mood.objects.filter(user=self.request.user).order_by('-date')

# -------------------------------
#           ERROR PAGES
# -------------------------------

def custom_404(request, exception):
    """Custom 404 error page."""
    return render(request, 'errors/404.html', status=404)

def custom_403(request, exception):
    """Custom 403 error page."""
    return render(request, 'errors/403.html', status=403)