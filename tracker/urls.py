from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('workouts/', views.workout_list, name='workout_list'),
    path('workout/add/', views.add_workout, name='add_workout'),
    path('workout/edit/<int:workout_id>/', views.edit_workout, name='edit_workout'),
    path('workout/delete/<int:workout_id>/', views.delete_workout, name='delete_workout'),
    path('moods/', views.mood_list, name='mood_list'),
    path('mood/add/', views.mood_create, name='mood_create'),
]
