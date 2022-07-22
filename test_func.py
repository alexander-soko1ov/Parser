import re
import random
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

# print('Введите строку:')
string = 'Основы_Python_в_четверг_15:00 в среду 15:00 '
cprint(string, 'green')

'''
добавить функцию проверки времени времени в сообщении и времени сейчас, если время в сообщении больше, 
то переводить дату на следующую

добавить функцию прибавления к времени сейчас времени из фраз в тексте 'через час, минуту и т.д.' 

добавить сюда функцию определения фраз 'на неделе, на выходных'

добавить сюда функцию определения дат по дням недели

разобраться с number из данного текста 'тренировка каждый час в 20:19' выводится numbers = 21
'''


mount = None
numbers = None
hour = None
minutes = None
each = None
word_number = None
day_of_the_week = None
datetime_element_on_right = None
month_or_numbers = None
on_the_week = None
hour_str = 0
minutes_str = 0


through_time = None
at_the_time = None

'''
время и дата сейчас
'''
datetime_today = datetime.datetime.today()
# print('Сейчас: ', time_today)
weekday_today = datetime_today.weekday()
year = datetime_today.year
mount_data = datetime_today.month
numbers = datetime_today.day
hour = datetime_today.hour
minutes = datetime_today.minute
date_difference = 0
days_week = None
weeks = 0

days_of_the_week = {
    'понедельник': 0,
    'вторник': 1,
    'среда': 2,
    'четверг': 3,
    'пятница': 4,
    'суббота': 5,
    'воскресенье': 6
}

dictionary_month = {
    'январь': 1,
    'февраль': 2,
    'март': 3,
    'апрель': 4,
    'май': 5,
    'июнь': 6,
    'июль': 7,
    'август': 8,
    'сентябрь': 9,
    'октябрь': 10,
    'ноябрь': 11,
    'декабрь': 12
}

dictionary_datetime = {
    'минута': 'minute',
    'час': 'hour',
    'день': 'day',
    'дне': 'day',
    'неделя': 'week',
    'месяц': 'month',
    'год': 'year'
}

prefix_dictionary = {
    'в': 1,
    'через': 2,
    'кажд': 3
}


def get_key_by_value(value, dictionary):
    result = None
    for element in dictionary:
        if dictionary[element] == value:
            result = element
    return result


def finding_matches(string_split, dictionary, data):
    for element in string_split:
        for element_dict in dictionary:
            if (element_dict[:-1] == element) or \
                    (element_dict == element) \
                    or (element_dict == element[:-1]) or \
                    (element_dict[:-1] == element[:-1]):
                if data == 1:
                    result = element_dict
                    data = dictionary[result]
                else:
                    data = element_dict
    return data


status = None
string_split = ''


# проверка статуса на условия и сплит строки (проблема с пробелами)
if isinstance(string, str):
    message = string.lstrip()
    string_split = string.lower().split()
    status = None

    for element_status_word in string_split[0]:
        # cprint(element_status_word, 'red')
        if element_status_word in ['/', '\\', 'd']:
            status = "Failure"
            break
        elif " " in element_status_word:
            status = "Success"
        else:
            status = "Success"
else:
    status = "Failure"

for element in string_split:
    element_on_right = None
    if element in ['каждое', 'каждую', 'каждый']:
        index_element = string_split.index(element) + 1
        element_on_right = string_split[index_element]
        each = element
        index_element_on_rigth = string_split.index(element_on_right)

        if not element_on_right.isdigit() and not (element_on_right in dictionary_datetime):
            day_of_the_week = finding_matches(string_split, days_of_the_week, 0)

        elif element_on_right.isdigit() and ((len(element_on_right) == 1) or (len(element_on_right) == 2)):
            numbers = element_on_right
            cprint(element_on_right, 'red')
            index_element_on_rigth = string_split.index(element_on_right)
            month_or_numbers = string_split[index_element_on_rigth + 1]

            if month_or_numbers in ['число']: # проверка на слово 'число'
                word_number = month_or_numbers
            else:   # проверка на месяц
                mount = finding_matches(string_split, dictionary_month, 0)
                mount_data = dictionary_month[mount]

        elif month_or_numbers in dictionary_month:
            mount = month_or_numbers
            mount_data = dictionary_month[mount]

        if element_on_right in dictionary_datetime:
            datetime_element_on_right = element_on_right

    elif element in ['в', 'во']:
        index_element = string_split.index(element) + 1
        element_on_right = string_split[index_element]
        each = element
        day_of_the_week = finding_matches(string_split, days_of_the_week, 0)

    elif element in ['на']:
        index_element = string_split.index(element) + 1
        element_on_right = string_split[index_element]
        each = element

        if ('-' in element_on_right) and (element_on_right.replace('-', '').isdigit()) and (len(element_on_right) in [3, 5]):
            for element_data in element_on_right:
                if element_data == '-':
                    index_data_l = element_on_right.index(element_data) - 1
                    index_data_r = element_on_right.index(element_data) + 1
                    if element_on_right[index_data_l].isdigit() and element_on_right[index_data_r].isdigit():
                        datetime_element_on_right = finding_matches(string_split, dictionary_datetime, 0)
                        numbers = element_on_right[index_data_l] + element_data + element_on_right[index_data_r]
                        # print(element, number, datetime_element_on_right)
        else:
            datetime_element_on_right = finding_matches(string_split, dictionary_datetime, 0)

    elif element in ['через', 'Через']:
        index_element = string_split.index(element) + 1
        element_on_right = string_split[index_element]
        each = element
        datetime_element_on_right = finding_matches(string_split, dictionary_datetime, 0)

    else:
        mount = finding_matches(string_split, dictionary_month, 0)
        if not mount == 0:
            mount_data = dictionary_month[mount]
        index_element = string_split.index(element) - 1
        element_on_left = string_split[index_element]
        if element_on_left.isdigit() and len(element_on_left) in [1, 2]:
            numbers = element_on_left

    for day_of_week in string_split:
        prefixes_day_of_week = day_of_week
        # cprint(finding_matches(string_split, days_of_the_week, 1), 'red')
        # определение дней недели
        date_def = finding_matches(string_split, days_of_the_week, 1)
        if date_def in [0, 1, 2, 3, 4, 5, 6]:

            day_of_week = get_key_by_value(date_def, days_of_the_week)
            if days_of_the_week[day_of_week] < weekday_today:
                date_difference = days_of_the_week[day_of_week] - weekday_today + 7
            elif days_of_the_week[day_of_week] == weekday_today:
                date_difference = days_of_the_week[day_of_week] - weekday_today + 7
            elif days_of_the_week[day_of_week] > weekday_today:
                date_difference = days_of_the_week[day_of_week] - weekday_today

    '''
    получение даты и времени из итогового значения
    '''
    number = datetime_today + datetime.timedelta(days=date_difference, weeks=weeks)
    year = number.year
    mount = number.month
    day = number.day
    hour = number.hour
    minutes = number.minute
    day_of_the_week = weekday_today


    for index_time, element_time in enumerate(string_split):
        if (':' in element_time) and (element_time.replace(':', '').isdigit()) and (len(element_time) in [4, 5]):
            word_before_element = string_split[index_time - 1]
            if len(element_time) == 4:
                hour_str = element_time[:-3]
                minutes_str = element_time[2:]

            else:
                hour_str = element_time[:-3]
                minutes_str = element_time[3:]

            if word_before_element in ['в', 'к']:
                # cprint("в, к", 'yellow')
                mask_str_time = word_before_element + ' ' + element_time
            else:
                mask_str_time = element_time

        else:
            element_time = None


# работа с datetime, получение года, месяца, даты и времени, исходя из изначальных условий
after_time = datetime.datetime(year=int(year), month=int(mount_data), day=int(numbers))

delta_time = datetime.timedelta(hours=int(hour_str), minutes=int(minutes_str))

time = None



if each in ['через', 'Через']:
    time = datetime_today + delta_time
    hour = time.hour
    minutes = time.minute
elif each in ['к', 'в']:
    time = after_time + delta_time
    hour = time.hour
    minutes = time.minute


'''
получение даты и времени из итогового значения
'''

print(day, mount, year)
# print(hour, ":", minutes)


print('Время: ', time)

print('статус: ', status)

if status == 'Success':
    print('индекс: ', each)
    # print(word_number)
    print('число: ', numbers)
    print('часы: ', hour)
    print('минуты: ', minutes)
    print('день недели: ', day_of_the_week)
    print('месяц: ', mount)
    print('час, месяц, год и.д.: ', datetime_element_on_right)
    # print('на: ', on_the_week)

print('\n')