from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from .forms import VideoForm
from django.contrib import messages
from .models import Video

# homepage view
def home(request):
    # make app name variable to display on homepage
    app_name = 'Music Videos'
    return render(request, 'video_collection/home.html', {'app_name': app_name})

# to add new video
def add(request):
    # get request to get page or post request to create a new video
    if request.method == 'POST':
        new_video_form = VideoForm(request.post)
        if new_video_form.is_valid():
            try:
                # if form data is valid - save to database
                new_video_form.save()
                return redirect('video_list')
                # messages.info(request, 'New video saved')
            
            except ValidationError:
                messages.warning(request, 'Invalid YouTube url')
            except IntegrityError:
                messages.warning(request, 'Video already in database')

        messages.warning(request, 'Please check data entered')
        # return same form with input if a validation error occurred
        return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})

    # requests video form from for model
    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})

# produce list of videos
def video_list(request):
    # grab all video objects from database
    videos = Video.objects.all()
    return render(request, 'video_collection/video_list.html', {'videos': videos})
