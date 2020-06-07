from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from meetings.models import Meeting

def welcome(request):
    #return HttpResponse("welcome to the meeting Planner")
    tmp_data = "Tanvir Rahman"
    total_meeting = Meeting.objects.count()
    return render(request,"website/welcome.html",{'tmp_data':tmp_data,'total_meeting':total_meeting})
def date(request):
    return HttpResponse("This page is erved at "+str(datetime.now()))

def about(request):
    return HttpResponse("This is about page")
