from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Link, Click
from django.conf import settings



# Create your views here.
def links(request, id):
    context = {
        "name": settings.NAME
    }
    try:
        result = Link.objects.get(name=id)
    except Link.DoesNotExist:
        return render(request, '404.html', context)
    newclick = Click(link=result)
    newclick.save()
    print(result.click_set.all())
    if not result.instant_redirect:
        context["url"] = result.url
        return render(request, 'noninstant.html', context)
    return HttpResponseRedirect(result.url)
