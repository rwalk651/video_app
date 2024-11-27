# urls for each in the app - each page needs URL, View, and Template

from django.urls import path
from . import views

# url paths that lead to pages
urlpatterns = [
    # homepage
    path('', views.home, name='home'),
    # page for adding videos
    path('add', views.add, name='add_video'),
    # page containing list of videos
    path('video_list', views.video_list, name='video_list')
]