from os import name
from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('edit/<slug:name>', views.url_view, name='editurl'),
    path('edit/', views.url_create, name='createurl'),
    path('delete/', views.delete_url, name='deleteurl')
]