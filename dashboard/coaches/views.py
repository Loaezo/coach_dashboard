from django.shortcuts import render, redirect
from coaches.models import Coach
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated:
        return redirect('ListCoaches')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('ListCoaches')
            else:
                return render(request, 'login_view.html',{'error':'Nombre de usuario y/o contraseña incorrectos'})
        return render(request, 'login_view.html',{'message':'OK'})

def logout_view(request):
    logout(request)
    return redirect('Login')


@login_required(login_url='Login')
def list_coaches(request):
    coaches = Coach.objects.all()
    return render(request,
        'CoachList.html',
        {'coaches':coaches}) 

def home(request):
    return render(request,
        'home.html') 
