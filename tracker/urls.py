from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import MoodUpdateView, MoodDeleteView, MoodListView

urlpatterns = [
    path('', views.home, name='home'),
    path('workout_list/', views.workout_list, name='workout_list'),
    path('workout/add/', views.add_workout, name='add_workout'),
    path('workout/edit/<int:workout_id>/', views.edit_workout, name='edit_workout'),
    path('workout/delete/<int:workout_id>/', views.delete_workout, name='workout_delete'),
    path('moods/', MoodListView.as_view(), name='mood_list'),
    path('moods/<int:pk>/edit/', MoodUpdateView.as_view(), name='mood_edit'),
    path('moods/<int:pk>/delete/', MoodDeleteView.as_view(), name='mood_delete'),
    path('mood/add/', views.mood_create, name='mood_create'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]
