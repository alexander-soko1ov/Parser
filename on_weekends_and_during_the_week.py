import random
import datetime
from termcolor import colored, cprint

string = 'фывф ф фыв ф 123 фыв 3 на неделе'

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

def get_key_by_value(value, dictionary):
    result = None
    for element in dictionary:
        if dictionary[element] == value:
            result = element
    return result

weekday_today = datetime.datetime.today().weekday()

weekday = None
index_week = None
week_weekend = None

for element in string_split:
    if element in ['по', 'на', 'в']:
        index_element_right = string_split.index(element) + 1
        element_right = string_split[index_element_right]
        index_week = finding_matches(string_split, week_weekend_dict, 1)
        mask_weekend = element + ' ' + element_right

if index_week == 1:
    weekday = random.randint(5, 6)
else:
    # с помощью datetime определить какой сейчас день недели в числовом представлении
    if weekday_today == 0:
        weekday = random.randint(1, 3)  # 0 - рандом (1-3)
    elif weekday_today == 1:
        weekday = random.randint(2, 3)  # 1 - (2-3)
    elif weekday_today == 2:
        weekday = random.randint(3, 4)  # 2 - (3-4)
    elif weekday_today == 3:
        weekday = 4  # 3 - (4)
    else:
        weekday = random.randint(0, 2)  # 4, 5, 6 - (0-2)

print('Ввод: ', string)
print('Сегодня: ', get_key_by_value(weekday_today, days_of_the_week))
print('Уведомление на: ', get_key_by_value(weekday, days_of_the_week))