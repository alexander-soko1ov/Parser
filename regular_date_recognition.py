import re
from termcolor import colored, cprint

string = 'каждый месяц'

string_split = string.split()
print(string_split)

mount = None
numbers = None
each = None
word_number = None
day_of_the_week = None
datetime_element_on_right = None
month_or_numbers = None

days_of_the_week = {
    'понедельник': 1,
    'вторник': 2,
    'среда': 3,
    'четверг': 4,
    'пятница': 5,
    'суббота': 6,
    'воскресенье': 7
}

dictionary_month = {
        'января': 1,
        'февраля': 2,
        'март': 3,
        'апреля': 4,
        'мая': 5,
        'июня': 6,
        'июля': 7,
        'августа': 8,
        'сентября': 9,
        'октября': 10,
        'ноября': 11,
        'декабря': 12
}

dictionary_datetime = {
    'минуту': 'minute',
    'час': 'hour',
    'день': 'day',
    'неделю': 'week',
    'месяц': 'month',
    'год': 'year'
}

for element in string_split:
    element_on_right = None
    if element in ['каждое', 'каждую', 'каждый']:
        index_element = string_split.index(element) + 1
        element_on_right = string_split[index_element]

        each = element
        index_element_on_rigth = string_split.index(element_on_right)

        if not element_on_right.isdigit() and not (element_on_right in dictionary_datetime):
            for element_days_of_the_week in days_of_the_week:
                if (element_days_of_the_week[:-1] == element_on_right) or \
                        (element_days_of_the_week == element_on_right) \
                        or (element_days_of_the_week == element_on_right[:-1]) or \
                        (element_days_of_the_week[:-1] == element_on_right[:-1]):
                    day_of_the_week = element_days_of_the_week

        elif element_on_right.isdigit() and ((len(element_on_right) == 1) or (len(element_on_right) == 2)):
            numbers = element_on_right
            index_element_on_rigth = string_split.index(element_on_right)
            month_or_numbers = string_split[index_element_on_rigth + 1]

            if month_or_numbers in ['число']: # проверка на слово 'число'
                    word_number = month_or_numbers
            else:   # проверка на месяц
                for element_dictionary_month in dictionary_month:
                    if (element_dictionary_month[:-1] == month_or_numbers) or \
                            (element_dictionary_month == month_or_numbers) \
                            or (element_dictionary_month == month_or_numbers[:-1]) or   \
                            (element_dictionary_month[:-1] == month_or_numbers[:-1]):
                        mount = element_dictionary_month

        elif month_or_numbers in dictionary_month:
            mount = month_or_numbers

        if element_on_right in dictionary_datetime:
            datetime_element_on_right = element_on_right

    elif element in ['в']:
        index_element = string_split.index(element) + 1
        element_on_right = string_split[index_element]
        each = element
        for element_days_of_the_week in days_of_the_week:
            if (element_days_of_the_week[:-1] == element_on_right) or \
                    (element_days_of_the_week == element_on_right) \
                    or (element_days_of_the_week == element_on_right[:-1]) or (
                    element_days_of_the_week[:-1] == element_on_right[:-1]):
                day_of_the_week = element_days_of_the_week
    else:
        pass

# print(str(each) + ' ' + str(day_of_the_week))
# print(str(each) + ' ' + str(numbers) + ' ' + str(word_number))
# print(str(each) + ' ' + str(numbers) + ' ' + str(mount))

print(each)
print(word_number)
print('число: ', numbers)
print('день недели: ', day_of_the_week)
print('месяц: ', mount)
print('час, месяц, год и.д.: ', datetime_element_on_right)