from django.shortcuts import render, get_object_or_404, redirect
from .models import Workout, MoodEntry
from .forms import WorkoutForm, MoodEntryForm

def workout_list(request):
    return render(request, 'tracker/workout_list.html')

def workout_detail(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    return render(request, 'tracker/workout_detail.html', {'workout': workout})

def workout_create(request):
    return render(request, 'tracker/workout_form.html')  # použij přesný název šablony, kterou máš

def workout_edit(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == "POST":
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            workout = form.save()
            return redirect('workout_detail', pk=workout.pk)
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'tracker/workout_form.html', {'form': form})

def workout_delete(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == "POST":
        workout.delete()
        return redirect('workout_list')
    return render(request, 'tracker/workout_confirm_delete.html', {'workout': workout})

def mood_list(request):
    moods = MoodEntry.objects.order_by('-date')
    return render(request, 'tracker/mood_list.html', {'moods': moods})

def mood_create(request):
    if request.method == 'POST':
        form = MoodEntryForm(request.POST)
        if form.is_valid():
            mood_entry = form.save(commit=False)
            mood_entry.user = request.user  # Přidá přihlášeného uživatele
            mood_entry.save()
            return redirect('mood_list')
    else:
        form = MoodEntryForm()
    return render(request, 'tracker/mood_form.html', {'form': form})

def home(request):
    return render(request, 'tracker/home.html')

