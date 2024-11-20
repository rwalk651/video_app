from django.shortcuts import render
from .forms import VideoForm

# homepage view
def home(request):
    # make app name variable to display on homepage
    app_name = 'Music Videos'
    return render(request, 'video_collection/home.html', {'app_name': app_name})

# to add new video
def add(request):
    # requests video form from for model
    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})
