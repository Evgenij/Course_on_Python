import os
from glob import iglob
import pathlib
import subprocess
import re
import shutil

'''Задание 7. Написать скрипт trackmix.py, который формирует обзорный трек-микс
           альбома (попурри из коротких фрагментов mp3-файлов в
           пользовательской директории). Для манипуляций со звуковыми
           файлами можно использовать сторонние утилиты, например, FFmpeg.
           Пример вызова и работы скрипта:
           trackmix --source "C:\Muz\Album" --count 5 --frame 15 -l -e
           --- processing file 1: 01 - Intro.mp3
           --- processing file 2: 02 - Outro.mp3
           --- done!
           Параметры скрипта:
           --source (-s) – имя рабочей директории с треками, обязателен;
           --destination (-d) – имя выходного файла, необязателен (если не указан,
           то имя выходного файла – mix.mp3 в директории source);
           --count (-c) – количество файлов в "нарезке", необязателен (если он не
           указан, то перебираются все mp3-файлы в директории source);
           --frame (-f) – количество секунд на каждый файл, необязателен (если не
           указан, скрипт вырезает по 10 секунд из произвольного участка каждого
           файла);
           --log (-l) – необязательный ключ (если этот ключ указывается, то скрипт
           должен выводить на консоль лог процесса обработки файлов, как в
           примере);
           --extended (-e) – необязательный ключ (если этот ключ указывается, то
           каждый фрагмент попурри начинается и завершается небольшим
           fade in/fade out).
'''

def make_mix(source, destination='', count=4, frame = 10, l = True, e = True):

    out = open('log.txt', 'w') #Открываем файл для сохранения логов выполнения
    files = list(pathlib.Path(source).glob("*.mp3")) #Собираем список файлов

    if destination == '': #Если destination не указан
        destination = source #Используем директорию source
    if count == 0: #Если кол-во файлов не указано
        count = len(files) #Используем все файлы

    #Создание фрагментов отдельных файлов
    if not(pathlib.Path(source+r"\mixes").exists()): #Все фрагменты заносим в папку mixes
        os.mkdir(source + r"\mixes")

    for index in range(count):
        command = 'ffmpeg.exe -i "'+str(files[index])+'" -hide_banner' #Задаем команду на получение длительности файла
        text = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) #Читаем вывод
        text = text.stdout.read().decode('cp866') #Декодируем вывод
        duration = re.compile("\d\d:\d\d:\d\d.\d\d").search(text).group() #Получаем строку Duration: 'время'
        minutes = int(duration.split(':')[1]) #Получаем количество полных минут длительности
        seconds = round(float(duration.split(':')[2])) #Получаем количество секунд длительности
        time = minutes*60+seconds #Вычисляем длительность в секундах
        time = round(time/100*10) #Считаем 10% от длительности, с той секунды будет начинаться трек

        if e == True:
            command = 'ffmpeg.exe -ss '+str(time)+' -t '+str(frame)+' -i "' +\
                      str(files[index])+'" -filter:a "afade=in:st=0:d=2, afade=out:st='+str(frame-2) +\
                      ':d=2" -y "mixes\mix'+str(index)+'.mp3"' #Это команда с добавлением fade in/out эффекта
        else:
            command = 'ffmpeg.exe -ss ' + str(time) + ' -t ' + str(frame) + ' -i "' + \
                      str(files[index]) + '" -y "mixes\mix' +\
                      str(index) + '.mp3"'  # Это команда без добавления fade in/out эффекта
        if l == True: #Если log - True выводим логи
            print('---processing file '+str(index)+': '+str(os.path.split(files[index])[-1]))
            subprocess.Popen(command, stdout=out, stderr=out) #Выполняем команду, в папке destination появится файл mixes.mp3

    os.chdir(source + os.sep + r'\mixes')  # Переход в папку с миксами
    files = os.listdir(os.getcwd())  # Получаем список миксов
    command = 'ffmpeg -i "concat:' + '|'.join(files) + '" -c copy MainMix.mp3'  # Формируем команду для объединения файлов
    subprocess.call(command)  # Выполняем команду
    out.close()  # Закрываем файл сохранения логов

make_mix(os.getcwd(),"",4,10,True,True)

