from django.shortcuts import render

# homepage view
def home(request):
    # make app name variable to display on homepage
    app_name = 'Music Videos'
    return render(request, 'video_collection/home.html', {'app_name': app_name})
