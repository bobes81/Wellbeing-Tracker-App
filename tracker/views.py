from django.shortcuts import render
from datetime import datetime

def home(request):
    now = datetime.now()
    return render(request, 'tracker/home.html', {'now': now})
