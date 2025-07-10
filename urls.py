from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # ← Přidáno pro registraci a přihlášení
    path('', include('tracker.urls')),           # ← Zůstává pro homepage atd.
]