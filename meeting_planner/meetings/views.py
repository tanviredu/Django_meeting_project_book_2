from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Meeting


def meeting_list(request):
    meetings = Meeting.objects.all();
    return render(request,'meeting/list.html',{'meetings':meetings})


def meeting_detail(request,id):
    #meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting,pk=id)
    return render(request,'meeting/detail.html',{'meeting':meeting})
