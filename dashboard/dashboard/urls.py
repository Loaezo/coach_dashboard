# Imports de Django
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from coaches import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('coaches/', views.coaches),
]
