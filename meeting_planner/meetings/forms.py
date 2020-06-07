from django import forms
from .models import Meeting

class MeetingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MeetingForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {'class': 'form-control',}
        self.fields['date'].widget.attrs = {'class': 'form-control','type':'date'}
        self.fields['start_time'].widget.attrs = {'class': 'form-control','type':'Time'}
        self.fields['duration'].widget.attrs = {'class': 'form-control',}
        self.fields['room'].widget.attrs = {'class': 'form-control',}

    class Meta:
        model = Meeting

        fields = ('title','date','start_time','duration','room')
