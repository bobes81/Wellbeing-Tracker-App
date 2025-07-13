from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('workout_list/', views.workout_list, name='workout_list'),
    path('add_workout/', views.add_workout, name='add_workout'),
    path('edit_workout/<int:pk>/', views.edit_workout, name='edit_workout'),
    path('delete_workout/<int:pk>/', views.delete_workout, name='delete_workout'),
    path('moods/', views.mood_list, name='mood_list'),
    path('moods/add/', views.mood_create, name='mood_create'),
    path('moods/edit/<int:pk>/', views.mood_edit, name='mood_edit'),
    path('moods/delete/<int:pk>/', views.mood_delete, name='mood_delete'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]
