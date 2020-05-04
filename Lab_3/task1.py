class Fraction():

    def __init__(self, num, den):
	    # приватные переменные
        self.__num = num  # числитель
        self.__den = den  # знаменатель
        self.reduce() # метод сокращения дроби

    def __str__(self):  # Преборазования объекта в строку
	    # Если числитель и знаменатель одного знака
        if (self.__num < 0 and self.__den < 0) or (self.__num > 0 and self.__den > 0):
            return "%d/%d" % (abs(self.__num), abs(self.__den))  # Выводим дробь без минуса
        else:
            return "-%d/%d" % (abs(self.__num), abs(self.__den))  # Иначе с минусом

    def reduce(self):
        devider = self.gcd(self.__num, self.__den)  # Вычисляем найименьший общий делитель по алгоритму Евклида
        self.__num /= devider  # Делим числитель
        self.__den /= devider  # Делим знаменатель

    @staticmethod  # Статический метод
    def gcd(n, m):  # Алгоритм Евклида
        if m == 0:  # Если второе число ноль
            return n  # Возвращаем первое число
        else:
            return Fraction.gcd(m, n % m)  # Иначе вызываем эту же функцию, но меняем местами аргументы и первое число
            # делится по модулю на второе

    def __neg__(self):  # Перегрузка унарного оператора -
        return Fraction(-self.__num, self.__den)  # Возвращаем новый объект с обращенным знаком числителя

    def __invert__(self):  # Перегрузка унарного оператора бинарного инвертирования
        return Fraction(self.__den, self.__num)  # Меняем местами числитель и знаменатель

    def __pow__(self, power):  # Перегрузка оператора возведения в степень
        return Fraction(self.__num ** power, self.__den ** power)  # Возводим в степень числитель и знаменатель

    def __float__(self):  # Преобразование объекта в десятичную дробь
        return self.__num/self.__den  # Делим числитель на знаменатель

    def __int__(self):  # Преобразование объекта в целое число
        return int(self.__num/self.__den)  # Делим числитель и знаменатель и преобразовываем в целое


if __name__ == "__main__":
    fraction = Fraction(7, 2)
    print(-fraction)
    print(~fraction)
    print(fraction**2)
    print(float(fraction))
    print(int(fraction))
