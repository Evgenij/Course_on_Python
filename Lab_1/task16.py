import random
import itertools
import datetime

#сет для названий факультетов
teams = {'Физтех', 'Эконом', 'Мат.фак.', 'Хим.фак.',
         'Юр.фак.', 'Учфин.', 'ФИЯ', 'Ист.фак.',
         'Фил.фак.', 'Био.фак.', 'Mеж.фак.', 'Библ.',
         'Фак.доп.обр.', 'Проф.союз.', 'Медиацентр', 'Экон.кибер.'
}

#словарь для заполнения групп случайными командами
groups = {
    'group1': set(),
    'group2': set(),
    'group3': set(),
    'group4': set()
}

#цикл заполнения значений словаря групп
for group in groups.keys():
    # случайный список из 4ёх команд из сета факультетов
    groups[group] = set(random.sample(teams, 4))
    #перезаполнение сета факультетов отбрасывая уже выбранные ранее факультеты
    teams = set.difference(teams, groups[group])

#удаление сета факультетов
del(teams)

#формирование словаря 4 игр, по 2 факультета на 1 игру,
#комбинации длиной 2 из groups без повторяющихся факультетов
games = {'group1': list(itertools.combinations(groups['group1'], 2)),
         'group2': list(itertools.combinations(groups['group2'], 2)),
         'group3': list(itertools.combinations(groups['group3'], 2)),
         'group4': list(itertools.combinations(groups['group4'], 2))}

#установка дат игр начиная с 9 месяца и 14 числа в 22:45
game_date = datetime.datetime(2017, 9, 14, 22, 45)
#установка интервала между днями проведения игр
delta = datetime.timedelta(days=14)

#вывод списка игр по дням с указанием времени и даты
for i in range(6):
    print("День " + str(i+1))
    for game in games:
        date = '{0:02d}/{1:02d}/{2} {3}:{4}'.format(game_date.day,
                                                    game_date.month,
                                                    game_date.year,
                                                    game_date.hour,
                                                    game_date.minute)
        print('|{0}| vs |{1}|\tдата {2}'.format(games[game][i][0], games[game][i][1], date))
    game_date = game_date + delta