def convert(number):
    if ',' in number:
        string = number.split(',')
    else:
        string = number.split('.')

    if len(string[1]) == 2:
        print(string[0] + " руб. " + string[1] + " коп.")
    elif len(string[1]) == 1:
        print(string[0] + " руб. " + string[1] + "0 коп.")
    else:
        print("Вы ввели некорректные данные!\n")

flag = True
while flag:
    try:
        money = input("Введите число: ")
        if float(money) < 0:
            raise ValueError
        else:
            convert(money)
            flag = False

    except ValueError:
        print("Вы ввели некорректные данные!\n")
