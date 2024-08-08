# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import VideoStorage
import os
import cv2
import numpy as np
from .models import VideoStorage
from django.views.generic import ListView
from rstr.bstr import create_video_stream
from django.shortcuts import render

# Create your views here.


def runtext(request, stringrun):
    video = create_video_stream(stringrun)
    create_video = VideoStorage(title=video['title'], text=stringrun, video=video['video_path'])
    create_video.save()
    return render(request, 'video_created.html', {'title': create_video.title})

"""
    # Разрешение видео
    w, h = 400, 300
    # Задаём параметры - видеопоток с частотой 30 кадров в сек
    video = cv2.VideoWriter(f"videos/{stringrun}.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 30, (w, h))
    # Создаем кадр с фиолетовым фоном
    frame = np.zeros((h, w, 3), dtype=np.uint8)
    frame[:, :] = [255, 0, 255]

    # Устанавливаем параметры шрифта
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 5
    font_thickness = 5
    font_color = (255, 255, 255)

    # Получение размеров текста в пикселях
    message_length = cv2.getTextSize(stringrun, font, font_scale, font_thickness)[0][0]

    # Координаты для бегущей строки
    x, y = w, h // 2 + 30
    scroll_speed = int((message_length + w) / 90)


    while x + message_length > 0:
        # Очистка кадра
        frame.fill(0)
        frame[:, :] = [255, 0, 255]
        # Новые координаты для бегущей строки
        x -= scroll_speed  # Скорость бегущей строки
        cv2.putText(frame, stringrun, (x, y), font, font_scale, font_color, font_thickness)
        video.write(frame)

    # Закрываем видеопоток
    video.release()

"""



class VideoListView(ListView):
    """
    Представление списка видео
    """
    queryset = VideoStorage.objects.all().order_by('-created')
    context_object_name = 'videos'
    template_name = 'videolist.html'

