from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
def links(request, id):
    # TODO: Make redirect to correct page
    return HttpResponseRedirect("https://google.com")