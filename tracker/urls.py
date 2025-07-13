from django.urls import path
from django.contrib.auth.views import LoginView
from .views import (
    home, workout_list, add_workout, edit_workout, delete_workout,
    mood_list, mood_create, register, logout_view
)

urlpatterns = [
    path('', home, name='home'),
    path('workout_list/', workout_list, name='workout_list'),
    path('workout/add/', add_workout, name='add_workout'),
    path('workout/edit/<int:workout_id>/', edit_workout, name='edit_workout'),
    path('workout/delete/<int:workout_id>/', delete_workout, name='delete_workout'),
    path('moods/', mood_list, name='mood_list'),
    path('mood/add/', mood_create, name='mood_create'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
]
