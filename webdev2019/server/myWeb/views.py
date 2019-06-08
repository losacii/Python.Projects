from django.http import HttpResponse

def index(request):
    output="HI! This is the Index page!"
    return HttpResponse(output)