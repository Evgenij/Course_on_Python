import os
# -*- coding: utf-8 -*-

'''
Задание №1. Напишите скрипт, который читает текстовый файл и выводит символы
             в порядке убывания частоты встречаемости в тексте. Регистр символа
             не имеет значения. Программа должна учитывать только буквенные
             символы (символы пунктуации, цифры и служебные символы слудет
             игнорировать). Проверьте работу скрипта на нескольких файлах с
             текстом на английском и русском языках, сравните результаты с
             таблицами, приведенными в wikipedia.org/wiki/Letter_frequencies.
'''


def print_frequencies(filename):
    #создал словарь для хранения символов и их количества
    vocabulary = {}
    file = open(filename,encoding='utf-8')
    #занесение текста из файла в переменную
    text = ''.join([line.lower() for line in file.readlines()])
    #переменная для подсчета символов в тексте не считая пробелы и знаки пунктуации
    sum = 0
    for symbol in text:
        if symbol in vocabulary:
            vocabulary[symbol] +=1
            sum += 1
        else:
            if symbol.isalpha():
                vocabulary[symbol] = 1
                sum += 1
    #создал список из значений словаря
    freq = list(vocabulary.values())
    #отсортировал в порядке убывания значений
    freq.sort(reverse=True)
    alphabet = dict(sorted(vocabulary.items(), key = lambda item: item[1], reverse=True))
    print("Всего символов в тексте =",sum)
    for (key, value) in alphabet.items():
        print("Количество символов \"%s\" = %s и частота встречаемости символа равна %s" % (key, value, value/sum))
    file.close()

#изменИл текущий рабочий каталог на заданный Task1
os.chdir('Task1')
#вызвал функцию поиска встречаемости символов
print("Русский текст")
print_frequencies('textRus.txt')
print("\nАнглийский текст")
print_frequencies('textEng.txt')