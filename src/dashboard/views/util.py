from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse
from django.conf import settings


def forward_to_must_login(request: HttpRequest):
    request.session['loginpagealert'] = {
        'type': 'danger',
        'text': 'You must be logged in to do that!'
    }
    return HttpResponseRedirect(reverse('dashboard:login'))


def generatecontext(request: HttpRequest):
    return {
        'name': settings.NAME,
        'logged': request.user.is_authenticated
    }


def dangeralert(context, text):
    context['alert'] = {
        'type': 'danger',
        'text': text
    }
    return context
