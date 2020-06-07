from django.urls import path
from . import views

app_name='meetings'

urlpatterns = [
    path('create',views.create_meeting,name='create_meeting'),
    path('',views.meeting_list,name='meeting_list'),
    path('room_list',views.room_list,name='room_list'),
    path('detail/<int:id>',views.meeting_detail,name='meeting_detail'),


]
