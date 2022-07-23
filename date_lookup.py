import re
import datetime
from termcolor import colored, cprint


text_0 = "Начать собираться в 4:31"
text_1 = "Проснуться, улыбнуться, почистить зубы и помыться в 07:13"
text_2 = "Съездить на дачу 17 мая в 16:15"
text_3 = 'Подписать служебку у начальника 13 декабря 2021 года в 16:15'
text_4 = "Убраться в квартире через 90 минут"
text_5 = "Позвонить друзьям через 3 часа"
text_6 = "Приготовить покушать на 2-3 дня 3 сентября 2022 года в 06:01"
text_7 = "Перевод локального компьютера в режим гибернации завтра"
text_8 = "Выключить 13 декабря в 20:17"
text_9 = "Перевод локального компьютера в режим гибернации через 2 дня"
text_10 = 'Служебку подписать на питон 12 ноября утром'
text_11 = 'Служебку подписать на питон в четверг в 20:17'
text_12 = 'Служебку подписать на питон в среду'
text_13 = 'Служебку в отдел кадров в среду в 13:13'
text_14 = "В понедельник уроки"
text_15 = 'Поскольку все записи имеют один и тот же шаблон, внести данные, которые хотите извлечь из пары скобок 13 декабря 2022 года в 16:15'
text_16 = "Напомни про гречку через 14 минут"
text_17 = "Через 50 минут таймер установаить. дерзай"
text_18 = "Основы_Python_в_четверг_15:00 3 сентября 2022 года"
text_19 = " Основы_Python_в_четверг_15:00 в среду 15:00 "
text_20 = "13 1311"
text_21 = 1231
text_22 = "Сходить покушать на неделе в 13:13"
text_23 = "del_qustion_answer*как дела?*норма, как сам?"
text_24 = "Сходить покушать на неделе"
text_25 = "В следующем месяце Подписать служебку "
text_26 = "\d\de23 2\3 3r3556"
text_27 = "Подписать служебку по выходным"
text_28 = "Сходить в сауну каждое 28 число"
text_29 = "Подписать служебку по выходным в 20:19"
text_30 = "поздравить с др маму через год в 20:18"
text_31 = "поздравить с др маму через час"
text_32 = "тренировка каждый час в 20:19"
text_33 = "Подписать служебку 23 февраля"
text_34 = "Тренировка каждый понедельник"
text_35 = "Тренировка каждый день"



dictionary_datetime = {
        'минута': 1,
        'час': 2,
        'дня': 3,
        'неделя': 4,
        # 'месяц': 5,
        # 'год': 6
    }


def finding_matches(string_split, dictionary, text=0):
    """определяет дни недели, месяцы и другое, отбрасывая окончания,
    возвращает:
        0 - текcтовый элемент из словаря
        1 - элемент словаря по значению (в числовом представлении)
        2 - элемент, который совпал со словарём"""
    data = None
    for element in string_split:
        for element_dict in dictionary:
            if (element_dict[:-1] == element) or \
                    (element_dict == element) \
                    or (element_dict == element[:-1]) or \
                    (element_dict[:-1] == element[:-1]):

                if text == 1:
                    """вывод значения ключа из словаря"""
                    result = element_dict
                    data = dictionary[result]
                elif text == 0:
                    """вывод ключа словаря (элемента из словаря)"""
                    data = element_dict
                elif text == 2:
                    """вывод элемента из текста"""
                    data = element
                else:
                    data = None
    return data


def date_lookup(string_split):
    """функция определяет время написанное в текстовом виде, например:
    'через 5 минут, через 12 часов, через день, через неделю, через год'"""

    datetime_today = datetime.datetime.today()
    weekday = datetime_today.weekday()
    minute = datetime_today.minute
    hour = datetime_today.hour
    day = datetime_today.day
    mount = datetime_today.month
    year = datetime_today.year

    for element_date in string_split:
        if finding_matches(string_split, dictionary_datetime, 1) == 1:
            # минут
            element_message_split_left = string_split[string_split.index(element_date) - 1]
            if element_message_split_left.isdigit():
                minute_multiplier = int(element_message_split_left)
            else:
                minute_multiplier = 1
            datetime_minutes = datetime_today + datetime.timedelta(minutes=int(minute_multiplier))
            hour = datetime_minutes.hour
            minute = datetime_minutes.minute
            day = datetime_minutes.day

        elif finding_matches(string_split, dictionary_datetime, 1) == 2:
            # часов
            element_message_split_left = string_split[string_split.index(element_date) - 1]
            if element_message_split_left.isdigit():
                hour_multiplier = int(element_message_split_left)
            else:
                hour_multiplier = 1
            datetime_minutes = datetime_today + datetime.timedelta(hours=int(hour_multiplier))
            hour = datetime_minutes.hour
            day = datetime_minutes.day
            mount = datetime_minutes.month
        elif finding_matches(string_split, dictionary_datetime, 1) == 3:
            # дней
            element_message_split_left = string_split[string_split.index(element_date) - 1]
            if element_message_split_left.isdigit():
                day_multiplier = int(element_message_split_left)
            else:
                day_multiplier = 1
            datetime_minutes = datetime_today + datetime.timedelta(days=int(day_multiplier))
            day = datetime_minutes.day
            mount = datetime_minutes.month
        elif finding_matches(string_split, dictionary_datetime, 1) == 4:
            # недель
            element_message_split_left = string_split[string_split.index(element_date) - 1]
            if element_message_split_left.isdigit():
                weeks_multiplier = int(element_message_split_left)
            else:
                weeks_multiplier = 1
            datetime_minutes = datetime_today + datetime.timedelta(weeks=int(weeks_multiplier))
            day = datetime_minutes.day
            mount = datetime_minutes.month
        elif element_date in ['год', 'года', 'лет']:
            """лет"""

            element_message_split_left = string_split[string_split.index(element_date) - 1]

            if element_message_split_left.isdigit() and len(element_message_split_left) == [1, 2]:
                day_multiplier = int(element_message_split_left)

            elif element_message_split_left.isdigit() and len(element_message_split_left) == 4 and 2020 < int(element_message_split_left) < 2100:
                day_multiplier = int(element_message_split_left) - year
            else:
                day_multiplier = 1

            if year % 4 == 0:
                day_delta = 366 * day_multiplier
                datetime_minutes = datetime_today + datetime.timedelta(days=int(day_delta))
                day = datetime_minutes.day
                year = datetime_minutes.year
            else:
                day_delta = 365 * day_multiplier
                datetime_minutes = datetime_today + datetime.timedelta(days=int(day_delta))
                day = datetime_minutes.day
                year = datetime_minutes.year

    date = [day, mount, year, hour, minute]
    return date

for i in range(36):
    message_space = globals()[f'text_{i}']
    print(message_space)


    """проверка статуса на условия и сплит строки (проблема с пробелами)"""
    if isinstance(message_space, str):
        message = message_space.lstrip().lower()
        string_split = re.split(' ', message)
        status = None
        # print(message_split[0])

        for element_status_word in string_split[0]:
            # cprint(element_status_word, 'red')
            if element_status_word in ['/', '\\', 'd']:
                status = "Failure"
                break
            elif " " in element_status_word:
                status = "Success"
            else:
                status = "Success"
        cprint(string_split, 'green')
    else:
        status = "Failure"
        message_space = ''

    print(date_lookup(string_split))
    print('\n')