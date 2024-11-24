from pytube import YouTube



# Ввод URL видео

video_url = input('Введите URL видео >> ')

save_location = "./"  # Путь для сохранения видео



# Создание объекта YouTube

yt = YouTube(video_url)



# Настройка качества сохраняемого ролика (720p, прогрессивное скачивание)

stream = yt.streams.filter(res="720p", progressive=True).first()



# Скачивание видео

stream.download(output_path=save_location)

print('Видео успешно сохранено')