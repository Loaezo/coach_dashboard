from django.shortcuts import render

from django.http import HttpResponse

def coaches(request):
    coaches = ['John', 'Jane']
    return HttpResponse(str(coaches))