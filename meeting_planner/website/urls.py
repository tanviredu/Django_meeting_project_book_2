from django.urls import path
from . import views

app_name='website'

urlpatterns = [
        path('welcome',views.welcome,name='welcome'),
        path('date',views.date,name='date'),
        path('about',views.about,name='about'),
]
