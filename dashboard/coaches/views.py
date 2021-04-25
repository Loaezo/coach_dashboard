from django.shortcuts import render, redirect
from coaches.models import Coach
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# class HomeView():
# @login_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('ListCoaches')
        else:
            return render(request, 'login_view.html',{'error':'Invalid username and/or password'})
    return render(request, 'login_view.html',{'message':'OK'})

def list_coaches(request):
    coaches = Coach.objects.all()
    return render(request,
        'CoachList.html',
        {'coaches':coaches}) 

def home(request):
    return render(request,
        'home.html') 

       # template = get_template('login_view.html')
        # return render(template.render())
