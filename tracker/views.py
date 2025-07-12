from django.http import HttpResponse

def home(request):
    return HttpResponse("🌈 IT WORKS! — This is coming from views.py")
