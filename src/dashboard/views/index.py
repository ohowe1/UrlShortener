from django.http import HttpRequest
from django.shortcuts import render
from .util import *
from links.models import Link

def index(request: HttpRequest):
    context = generatecontext(request)
    if not context['logged']:
        return forward_to_must_login(request)
    if (request.session.get('indexalert')):
        context['alert'] = request.session.get('indexalert')
        del request.session['indexalert']
    context['links'] = Link.objects.all()
    return render(request, 'dashindex.html', context)