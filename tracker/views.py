from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.contrib.auth.models import User
from .models import Workout, Mood  # Import models from models.py
from .forms import WorkoutForm, MoodForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

def home(request):
    return render(request, 'tracker/home.html', {'now': now()})

@login_required
def workout_list(request):
    workouts = Workout.objects.filter(user=request.user).order_by('-date')
    return render(request, 'tracker/workout_list.html', {'workouts': workouts})

@login_required
def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm()
    return render(request, 'tracker/add_workout.html', {'form': form})

@login_required
def edit_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'tracker/edit_workout.html', {'form': form})

@login_required
def delete_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    if request.method == 'POST':
        workout.delete()
        return redirect('workout_list')
    return render(request, 'tracker/delete_workout.html', {'workout': workout})

@login_required
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

@login_required
def mood_list(request):
    moods = Mood.objects.filter(user=request.user).order_by('-date')
    return render(request, 'tracker/mood_list.html', {'moods': moods})

@login_required
def edit_mood(request, pk):
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
    mood = get_object_or_404(Mood, pk=pk, user=request.user)
    if request.method == 'POST':
        mood.delete()
        return redirect('mood_list')
    return render(request, 'tracker/mood_confirm_delete.html', {'mood': mood})

class MoodListView(ListView):
    model = Mood
    template_name = 'tracker/mood_list.html'
    context_object_name = 'moods'

    def get_queryset(self):
        return Mood.objects.filter(user=self.request.user).order_by('-date')

class MoodUpdateView(UpdateView):
    model = Mood
    form_class = MoodForm
    template_name = 'tracker/mood_form.html'
    success_url = reverse_lazy('mood_list')

    def get_queryset(self):
        return Mood.objects.filter(user=self.request.user)

class MoodDeleteView(DeleteView):
    model = Mood
    template_name = 'tracker/mood_confirm_delete.html'
    success_url = reverse_lazy('mood_list')

    def get_queryset(self):
        return Mood.objects.filter(user=self.request.user)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')