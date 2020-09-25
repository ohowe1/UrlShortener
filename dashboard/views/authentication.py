from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from .util import *

def login_view(request: HttpRequest):
    context = generatecontext(request)
    if context['logged']:
        return HttpResponseRedirect(reverse('index'))
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        if not username:
            context['alert'] = {
                'type': 'danger',
                'text': 'Username field required!'
            }
        elif not password:
            context['alert'] = {
                'type': 'danger',
                'text': 'Password field required!'
            }
        else:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                context['alert'] = {
                    'type': 'danger',
                    'text': 'Invalid credentials!'
                }
    else:
        alert = request.session.get('loginpagealert')
        if alert:
            context['alert'] = alert
            del request.session['loginpagealert']
    return render(request, 'login.html', context)


def logout_view(request: HttpRequest):
    if request.POST:
        logout(request)
        request.session['loginpagealert'] = {
            'type': 'success',
            'text': 'Logged out'
        }
        return HttpResponseRedirect(reverse('login'))
    return HttpResponse("You can only POST this page. We don't want it preloaded!")