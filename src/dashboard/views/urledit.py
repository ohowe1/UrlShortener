from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404
from links.models import Link
from django.core.validators import URLValidator
from .util import *


def assure_formname_and_url_not_null(formname: str, url: str, request: HttpRequest, context: dict):
    if not formname:
        context = dangeralert(context, 'Name field required!')
        return render(request, 'dashlink.html', context)
    if not url:
        context = dangeralert(context, 'URL field required!')
        return render(request, 'dashlink.html', context)
    return None


def assure_formname_is_not_in_use(formname: str, name: str, request: HttpRequest, context: dict):
    if not formname == name:
        try:
            Link.objects.get(name=formname)
            context = dangeralert(context, 'That name is already in use!')
            return render(request, 'dashlink.html', context)
        except:
            pass
    return None


def url_view(request: HttpRequest, name: str):
    context = generatecontext(request)
    if not context['logged']:
        return forward_to_must_login(request)
    if request.POST:
        return edit_url(request, name, context)
    try:
        link = Link.objects.get(name=name)
    except Exception:
        raise Http404
    context['link'] = link
    return render(request, 'dashlink.html', context)


def edit_url(request: HttpRequest, name: str, context: dict):
    link = None
    if name is not None:
        try:
            link = Link.objects.get(name=name)
        except Exception:
            raise Http404
    context['link'] = link
    if request.POST:
        formname = request.POST['name']
        url = request.POST['url']
        try:
            request.POST['instant']
            instant = True
        except:
            instant = False

        nullcheck = assure_formname_and_url_not_null(
            formname, url, request, context)
        if (nullcheck):
            return nullcheck
        del nullcheck
        formname = formname.replace(" ", "_")
        name_in_use = assure_formname_is_not_in_use(
            formname, name, request, context)
        if (name_in_use):
            return name_in_use
        del name_in_use

        try:
            URLValidator(None).__call__(url)
        except ValidationError:
            context = dangeralert(context, 'Thats not a valid URL!')
            return render(request, 'dashlink.html', context)
        try:
            if link is None:
                link = Link(url=url, name=formname, instant_redirect=instant)
            else:
                link.url = url
                link.name = formname
                link.instant_redirect = instant
            link.save()
        except Exception as e:
            print(e)
            context = dangeralert(context, 'An error has occured!')
            return render(request, 'dashlink.html', context)
        return HttpResponseRedirect(reverse('dashboard:index'))
    return HttpResponse("You can only POST this page.")


def url_create(request: HttpRequest):
    context = generatecontext(request)
    if not context['logged']:
        return forward_to_must_login(request)
    if request.POST:
        return edit_url(request, None, context)
    return render(request, 'dashlink.html', context)


def delete_url(request: HttpRequest):
    if request.POST:
        name = request.POST['urlname']
        try:
            link = Link.objects.get(name=name)
            link.delete()
            request.session['indexalert'] = {
                'type': 'success',
                'text': name + ' successfully deleted'
            }
        except:
            request.session['indexalert'] = {
                'type': 'danger',
                'text': 'An error has occured'
            }
    return HttpResponseRedirect(reverse('dashboard:index'))
