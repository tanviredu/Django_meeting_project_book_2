from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Meeting
from .models import Room
from .forms import MeetingForm


def meeting_list(request):
    meetings = Meeting.objects.all();
    return render(request,'meeting/list.html',{'meetings':meetings})


def meeting_detail(request,id):
    #meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting,pk=id)
    return render(request,'meeting/detail.html',{'meeting':meeting})

def room_list(request):
    rooms = Room.objects.all();
    return render(request,'meeting/room.html',{'rooms':rooms})

def create_meeting(request):
    new_meeting = None

    if request.method == "POST":
        meeting_form = MeetingForm(data=request.POST)

        if meeting_form.is_valid():
            new_meeting = meeting_form.save(commit=False)
            new_meeting.save()
    else:
        meeting_form = MeetingForm()

    return render(request,'meeting/create.html',{'new_meeting':new_meeting,'meeting_form':meeting_form})
