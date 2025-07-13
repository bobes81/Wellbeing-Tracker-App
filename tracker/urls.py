from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('workout_list/', views.workout_list, name='workout_list'),
    path('workout/add/', views.add_workout, name='add_workout'),
    path('workout/edit/<int:workout_id>/', views.edit_workout, name='edit_workout'),
    path('workout/delete/<int:workout_id>/', views.delete_workout, name='workout_delete'),
    path('moods/', views.mood_list, name='mood_list'),
    path('moods/add/', views.mood_create, name='mood_create'),
    path('moods/<int:pk>/edit/', views.edit_mood, name='edit_mood'),
    path('moods/<int:pk>/delete/', views.delete_mood, name='delete_mood'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]
