from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest
from django.conf import settings
from django.urls import reverse

# Create your views here.
def index(request: HttpRequest):
    if (request.user.is_authenticated):
        return HttpResponseRedirect(reverse('dashboard:index'))
    context = {
        'name': settings.NAME
    }
    return render(request, 'homepage.html', context)