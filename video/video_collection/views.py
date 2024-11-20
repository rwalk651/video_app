from django.shortcuts import render

# homepage view
def home(request):
    return render(request, 'video_collection/home.html')
