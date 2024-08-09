from django.http import HttpResponse
from .models import VideoStorage
from django.views.generic import ListView
from rstr.bstr import create_video_stream
from django.shortcuts import render

# Create your views here.


def base(request):
    return render(request, 'base.html')


def runtext(request, stringrun):
    video = create_video_stream(stringrun)
    create_video = VideoStorage(title=video['title'], text=stringrun, video=video['video_path'])
    create_video.save()
    response = HttpResponse(video, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{create_video.title}.mp4"'
    return response


class VideoListView(ListView):
    """
    Представление списка видео
    """
    queryset = VideoStorage.objects.all().order_by('-created')
    context_object_name = 'videos'
    template_name = 'videolist.html'