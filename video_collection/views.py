from django.shortcuts import render, redirect
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
            try:
                new_video_form.save() # Creates new Video object and saves
                return redirect('video_list')
                # todo redirect to list of videos
            except ValidationError:
                messages.warning(request, 'Invalid YouTube URL')
            except IntegrityError:
                messages.warning(request, 'You already added that video')
        
        messages.warning(request, 'Check the data entered')
        return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})

    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})


def video_list(request):
    videos = Video.objects.order_by('name')
    return render(request, 'video_collection/video_list.html', {'videos': videos})