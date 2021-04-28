# Imports de Django
from django.contrib import admin
from django.urls import path
# from django.http import HttpResponse

from coaches import views


urlpatterns = [
    path('', views.home, name='Home'),
    path('login/', views.login_view, name='Login'),
    path('logout/', views.logout_view, name='Logout'),
    path('admin/', admin.site.urls, name='Admin'),
    path('coaches/', views.list_coaches, name='ListCoaches'),

]
