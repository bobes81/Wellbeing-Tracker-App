from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('moods/', views.mood_list, name='mood_list'),
]
