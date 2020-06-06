from django.contrib import admin
from .models import Meeting,Room


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('title','date','start_time','duration','room')

    ## how you ncan filet or search the post in the adminpanel
    list_filter = ('title','date','start_time','duration','room')
    search_field = ('title','date','start_time','duration','room')


@admin.register(Room)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('name','floor','room_number')

    ## how you ncan filet or search the post in the adminpanel
    list_filter = ('name','floor','room_number')
    search_field = ('name','floor','room_number')
