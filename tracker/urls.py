from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('moods/', views.mood_list, name='mood_list'),
    path('workout/create/', views.workout_create, name='workout_create'),
    path('workouts/', views.workout_list, name='workout_list'),
    path('mood/create/', views.mood_create, name='mood_create'),
    path('add-mood/', views.add_mood_entry, name='add_mood_entry'),  # Verified URL
]
