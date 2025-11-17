from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # -------------------------------
    #              HOME
    # -------------------------------
    path('', views.home, name='home'),

    # -------------------------------
    #              MOODS
    # -------------------------------
    path('moods/', views.mood_list, name='mood_list'),
    path('moods/add/', views.add_mood, name='add_mood'),
    path('moods/edit/<int:pk>/', views.edit_mood, name='edit_mood'),
    path('moods/delete/<int:pk>/', views.delete_mood, name='delete_mood'),

    # -------------------------------
    #            WORKOUTS
    # -------------------------------
    path('workouts/', views.workout_list, name='workout_list'),
    path('workouts/add/', views.add_workout, name='add_workout'),
    path('workouts/edit/<int:pk>/', views.edit_workout, name='edit_workout'),
    path('workouts/delete/<int:pk>/', views.delete_workout, name='delete_workout'),

    # -------------------------------
    #         AUTHENTICATION
    # -------------------------------
    path('register/', views.register, name='register'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='accounts/login.html'),
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]