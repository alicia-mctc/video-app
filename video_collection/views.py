from django.shortcuts import render
from .models import Video
from .forms import VideoForm
from django.contrib import messages

# Create your views here.

def home(request):
    app_name = 'Exercise Videos'
    return render(request, 'video_collection/home.html', { 'app_name': app_name})

def add(request):
    if request.method == 'POST': # adding a new video
        new_video_form = VideoForm(request.POST)
        if new_video_form.is_valid():
            new_video_form.save() # Creates new Video object and saves
            messages.info(request, 'New video saved!')
            # todo redirect to list of videos
        else:
            messages.warning(request, 'Check the data entered')
            return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})

    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})

def video_list(request):
    videos = Video.objects.order_by('name')
    return render(request, 'video_collection/video_list.html', {'videos': videos})