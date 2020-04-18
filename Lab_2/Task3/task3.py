from pathlib import Path

'''Задание №3. Задан путь к директории с музыкальными файлами (в названии
             которых нет номеров, а только названия песен) и текстовый файл,
             хранящий полный список песен с номерами и названиями в виде строк
             формата «01. Freefall [6:12]». Напишите скрипт, который корректирует
             имена файлов в директории на основе текста списка песен.
'''

def rename_audio(folder, textfile):
    path = Path(folder)
    mask = '*.mp3'
    names = Path(textfile, encoding='utf-8')
    tracks = {}
    with names.open(encoding='utf-8') as file:
        for line in file:
            string = line.split('[')[0]
            tracks[string.split('.')[1].strip()] = string.strip()
    #print(tracks)

    for f in path.glob(mask):
        name = f.name.replace(f.suffix, '')
        try:
            f.rename(str(f).replace(name, tracks.get(name)))
        except TypeError:
            continue


rename_audio("audio", "names_audio.txt")