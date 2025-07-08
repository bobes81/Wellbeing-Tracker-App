from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('moods/', views.mood_list, name='mood_list'),
    path('workout/<int:pk>/', views.workout_detail, name='workout_detail'),
    path('workout/new/', views.workout_create, name='workout_create'),
    path('workout/<int:pk>/edit/', views.workout_edit, name='workout_edit'),
    path('workout/<int:pk>/delete/', views.workout_delete, name='workout_delete'),
]
