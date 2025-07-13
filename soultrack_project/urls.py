from django.contrib import admin
from django.urls import path, include
from tracker import views as tracker_views
from django.contrib.auth import views as auth_views
from django.conf.urls import handler403, handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracker.urls')),
    path('register/', tracker_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

handler404 = "tracker.views.error_404"
handler403 = "tracker.views.error_403"