from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:err>', views.fourofour, name='404')
]