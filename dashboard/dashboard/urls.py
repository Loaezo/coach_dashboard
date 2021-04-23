# Imports de Django
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from coaches.views import HomeView
from coaches import views


urlpatterns = [
    path('', HomeView.login, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('coaches/', HomeView.list_coach, name='coaches'),

]
