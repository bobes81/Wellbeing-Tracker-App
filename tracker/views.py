from django.shortcuts import render, redirect, get_object_or_404
from .models import Workout, Mood
from .forms import WorkoutForm, MoodForm
from django.utils.timezone import now

def home(request):
    return render(request, 'tracker/home.html', {'now': now()})

# WORKOUT VIEWS

def workout_list(request):
    workouts = Workout.objects.filter(user=request.user) if request.user.is_authenticated else []
    return render(request, 'tracker/workout_list.html', {'workouts': workouts})

def workout_create(request):
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

def workout_edit(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'tracker/workout_form.html', {'form': form})

def workout_delete(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    if request.method == 'POST':
        workout.delete()
        return redirect('workout_list')
    return render(request, 'tracker/workout_confirm_delete.html', {'workout': workout})

# MOOD VIEWS

def mood_list(request):
    moods = Mood.objects.filter(user=request.user) if request.user.is_authenticated else []
    return render(request, 'tracker/mood_list.html', {'moods': moods})

def mood_create(request):
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
