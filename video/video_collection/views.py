from django.shortcuts import render
from .forms import VideoForm
from django.contrib import messages

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
            # if form data is valid - save to database
            new_video_form.save()
            messages.info(request, 'New video saved')
        else:
            messages.warning(request, 'Please check data entered')
            # return same form with input if a validation error occurred
            return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})

    # requests video form from for model
    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})
