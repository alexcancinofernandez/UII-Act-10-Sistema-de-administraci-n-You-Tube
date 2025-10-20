from django.shortcuts import render, get_object_or_404, redirect
from .models import Video
from .forms import VideoForm

def index(request):
    return render(request, 'app_video_youtube/index.html', {'videos': Video.objects.all()})

def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'app_video_youtube/add.html', {'form': VideoForm(), 'success': True})
    else:
        form = VideoForm()
    return render(request, 'app_video_youtube/add.html', {'form': form})

def edit_video(request, id):
    video = get_object_or_404(Video, pk=id)
    if request.method == 'POST':
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return render(request, 'app_video_youtube/edit.html', {'form': form, 'success': True})
    else:
        form = VideoForm(instance=video)
    return render(request, 'app_video_youtube/edit.html', {'form': form})

def delete_video(request, id):
    video = get_object_or_404(Video, pk=id)
    if request.method == 'POST':
        video.delete()
        return redirect('index')
    return render(request, 'app_video_youtube/delete.html', {'video': video})
