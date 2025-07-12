from django.http import HttpResponse

def home(request):
    return HttpResponse("TESTING DIRECT RESPONSE — IF YOU SEE THIS, VIEWS ARE WORKING.")

# ostatní funkce klidně dočasně vynecháme pro test
