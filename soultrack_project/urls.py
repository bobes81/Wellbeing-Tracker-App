from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracker.urls')),  # Your app
    path('', include('django.contrib.auth.urls')),  # Login, logout, password_reset, etc.
]

# Error views (uncomment if needed later)
# handler403 = "tracker.views.custom_403"
# handler404 = "tracker.views.custom_404"