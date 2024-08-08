import cv2
import numpy as np


def create_video_stream(stringrun: str):
    savepath = f"strview/videos/{stringrun[:20]}.mp4"
    # Разрешение видео
    w, h = 400, 300
    # Задаём параметры - видеопоток с частотой 30 кадров в сек
    video = cv2.VideoWriter(savepath, cv2.VideoWriter_fourcc(*'mp4v'), 30, (w, h))
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
    return {'title': stringrun, 'video_path': savepath}


def main():
    text = input('Введите текст: ')
    create_video_stream(text)


if __name__ == '__main__':
    main()
