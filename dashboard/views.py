from django.shortcuts import render
from django.urls import reverse, resolve
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def generatecontext(request: HttpRequest):
    return {
        'name': settings.NAME,
        'logged': request.user.is_authenticated
    }


def index(request: HttpRequest):
    context = generatecontext(request)
    if not context['logged']:
        return forward_to_must_login(request)
    return render(request, 'dashindex.html', context)

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
    return HttpResponse("You can only POST this page. We don't want it preloaded! 🤦‍♂️")



def forward_to_must_login(request: HttpRequest):
    request.session['loginpagealert'] = {
        'type': 'danger',
        'text': 'You must be logged in to do that!'
    }
    return HttpResponseRedirect(reverse('login'))
