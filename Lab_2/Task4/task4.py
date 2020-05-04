import re

'''Задание4. Напишите скрипт, который позволяет ввести с клавиатуры имя
          текстового файла, найти в нем с помощью регулярных выражений все
          подстроки определенного вида, в соответствии с вариантом. Например,
          для варианта № 1 скрипт должен вывести на экран следующее:
          Строка 3, позиция 10 : найдено '11-05-2014'
          Строка 12, позиция 2 : найдено '23-11-2014'
          Строка 12, позиция 17 : найдено '23-11-2014'
'''

#Эта функция ищет даты в формате 22-01-2018
def find_dates(file):
    text = [string.strip() for string in open(file, 'r', encoding="utf-8").readlines()]
    pattern = re.compile('\d\d-\d\d-\d\d\d\d')
    dates = {}

    for index, string in enumerate(text):
        matches = pattern.finditer(string)
        for match in matches:
            dates["Строка "+str(index+1)+", позиция "+str(match.start())]=" : найдено '"+match.group()+"'"

    for key in dates.keys():
        print(key+dates[key])


find_dates("text.txt")
input()