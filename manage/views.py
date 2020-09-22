from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
# Create your views here.
def index(request):
    context = {'name': settings.NAME}
    return render(request, "home.html", context)

def fourofour(request, err):
    return render(request, "manage404.html")