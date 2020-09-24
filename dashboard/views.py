from django.shortcuts import render
from django.urls import reverse, resolve
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.


def generatecontext(request):
    return {
        'name': settings.NAME,
        'logged': request.user.is_authenticated
    }


def index(request):
    context = generatecontext(request)
    if not context['logged']:
        return forwardtologin(request)
    return render(request, 'dashindex.html', context)


def login(request):
    context = generatecontext(request)
    if (request.session.get('loginalert')):
        del request.session['loginalert']
        context['alert'] = {
            'type': 'danger',
            'text': 'You need to be logged in to do that!'
        }
    return render(request, 'login.html', context)


def forwardtologin(request):
    request.session['loginalert'] = True
    return HttpResponseRedirect(reverse('login', ))
