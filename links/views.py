from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Link


# Create your views here.
def links(request, id):
    try:
        result = Link.objects.get(name=id)
    except Link.DoesNotExist:
        return render(request, '404.html')
    print(result)
    result.clicks += 1
    result.save()
    return HttpResponseRedirect(result.url)
