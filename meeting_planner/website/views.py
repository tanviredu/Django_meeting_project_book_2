from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("welcome to the meeting Planner")

def date(request):
    return HttpResponse("This page is erved at "+str(datetime.now()))

def about(request):
    return HttpResponse("This is about page")
