import random
import datetime
from termcolor import colored, cprint

string = 'на выходных'

string_split = string.split()

days_of_the_week = {
    'понедельник': 0,
    'вторник': 1,
    'среда': 2,
    'четверг': 3,
    'пятница': 4,
    'суббота': 5,
    'воскресенье': 6
}

week_weekend_dict = {
    'выходным': 1,
    'неделе': 2
}

'''
функция определения совпадений слова из строки со словарём 
не обращая внимания на его окончание
'''

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

'''
функция определения ключа по значению в словаре
'''

def get_key_by_value(value, dictionary):
    result = None
    for element in dictionary:
        if dictionary[element] == value:
            result = element
    return result


def on_weekends(string_split, dictionary, dictionary_day_of_week, number_date=0, mask_date=0):
    """функция определения фраз 'на выходных, по выходным, на неделе'
    выводит день недели в числовом или текстовом представлении """

    """день недели сейчас"""
    datetime_today = datetime.datetime.today()
    weekday_today = datetime_today.weekday()

    index_week = None
    mask_weekend = None
    result = None

    for element in string_split:
        if element in ['по', 'на', 'в']:
            index_element_right = string_split.index(element) + 1
            element_right = string_split[index_element_right]
            index_week = finding_matches(string_split, dictionary, 1)
            mask_weekend = element + ' ' + element_right

    if index_week == 1:
        weekday = random.randint(5, 6)
    else:
        # с помощью datetime определить какой сейчас день недели в числовом представлении
        if weekday_today == 0:
            weekday = random.randint(1, 3)  # 0 - рандом (1-3)
        elif weekday_today == 1:
            weekday = random.randint(2, 3)  # 1 - рандом (2-3)
        elif weekday_today == 2:
            weekday = random.randint(3, 4)  # 2 - рандом (3-4)
        elif weekday_today == 3:
            weekday = 4  # 3 - (4)
        else:
            weekday = random.randint(0, 2)  # 4, 5, 6 - рандом (0-2)

    if number_date == 0:
        result = get_key_by_value(weekday, dictionary_day_of_week)
    if number_date == 1:
        result = weekday_today
    if mask_date == 1:
        result = mask_weekend

    return result

print('Ввод: ', string)
# print('Сегодня: ', on_weekends)
print('Уведомление на: ', on_weekends(string_split, week_weekend_dict, days_of_the_week, 0, 0), on_weekends(string_split, week_weekend_dict, days_of_the_week, 1, 0))
print('Маска: ', on_weekends(string_split, days_of_the_week, week_weekend_dict, 0, 1))