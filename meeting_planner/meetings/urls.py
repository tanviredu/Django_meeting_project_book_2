from django.urls import path
from . import views

app_name='meetings'

urlpatterns = [
    path('',views.meeting_list,name='meeting_list'),
    path('detail/<int:id>',views.meeting_detail,name='meeting_detail'),


]
