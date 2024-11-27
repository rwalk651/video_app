# describe how to show a form to display on a webpage

from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    # display fields from Video class
    class Meta:
        model = Video
        # list of fields matching names in Video model
        fields = ['name', 'url', 'notes']


class SearchForm(forms.Form):
    search_term = forms.CharField()