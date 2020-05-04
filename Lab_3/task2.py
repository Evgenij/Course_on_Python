import re

class Book():

    def __init__(self, author, title, code=None):
        if (title == '') or (type(title) != str):  # Если название книги - пустая строка или вообще не строка
            raise ValueError
        else:
            self.__title = title  # Иначе сохраняем название
        if (author == '') or (type(author) != str):  # То же самое для автора
            self.__author = 'Unknown'
        else:
            self.__author = author
        self.__code = code

    def tag(self):  # Реализация Taggable интерфейса
        return re.compile('[A-Z][a-z]+').findall(self.__title)  # Ищем слова с большой буквы и возвращаем их список

    def set_code(self, code):  # Функция установки кода книги
        self.__code = code

    def __str__(self):  # Преобразование в тип string
        return "[%s] %s '%s'" % (str(self.__code), self.__author, self.__title)


class Library():
    code = 1  # Cтатическая переменная - код книги

    def __init__(self, number, address):
        self.__number = number  # Номер библиотеки
        self.__address = address  # Адрес библиотеки
        self.__books = []  # Список книг

    def __iadd__(self, b):  # Перегрузка оператора +=
        b.set_code(self.code)  # установка кода книге
        self.code += 1
        self.__books.append(b)  # Дополняем список книг
        return self  # Возвращаем объект новой библиотеки

    def __iter__(self):  # Преобразование в итерируемый объект
        return iter(self.__books)  # Преобразуем список книг в итератор


if __name__ == "__main__":

    lib = Library(1, '51 Some str. NY')
    lib += Book('Leo Tolsoti', 'War and Peace')
    lib += Book('Charles Dickens', 'David Copperfield')

    for book in lib:
        print(book)
        print(book.tag())