from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler403, handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracker.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Django auth views for login/logout
]

handler403 = "tracker.views.custom_403"
handler404 = "tracker.views.custom_404"