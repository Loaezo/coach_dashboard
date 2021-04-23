from django.shortcuts import render
from coaches.models import Coach
from django.template.loader import get_template
from django.http import HttpResponse

class HomeView():

    def login(self):
        template = get_template('login.html')
        return HttpResponse(template.render())

    def list_coach(request):
        coaches = Coach.objects.all()
        return render(request,
            'CoachList.html',
            {'coaches':coaches})
    
