from django.http import HttpResponse

def home(request):
    return HttpResponse("🌟 YES! HEROKU DEPLOY WORKED — VIEW IS ACTIVE 🌟")

# ostatní funkce klidně dočasně vynecháme pro test
