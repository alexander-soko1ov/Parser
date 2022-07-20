import re
from termcolor import colored, cprint


# print('Введите строку:')
string = 'в понедельник 12 декабря'
print(string)


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
    'минута': 'minute',
    'час': 'hour',
    'день': 'day',
    'дне': 'day',
    'неделя': 'week',
    'месяц': 'month',
    'год': 'year'
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


status = None
string_split = ''


# проверка статуса на условия и сплит строки (проблема с пробелами)
if isinstance(string, str):
    message = string.lstrip()
    string_split = re.split(' ', message)
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
            index_element_on_rigth = string_split.index(element_on_right)
            month_or_numbers = string_split[index_element_on_rigth + 1]

            if month_or_numbers in ['число']: # проверка на слово 'число'
                word_number = month_or_numbers
            else:   # проверка на месяц
                mount = finding_matches(string_split, dictionary_month, 0)

        elif month_or_numbers in dictionary_month:
            mount = month_or_numbers

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
        index_element = string_split.index(element) - 1
        element_on_left = string_split[index_element]
        if element_on_left.isdigit() and len(element_on_left) in [1, 2]:
            numbers = element_on_left

    for index_time, element_time in enumerate(string_split):
        if (':' in element_time) and (element_time.replace(':', '').isdigit()) and (len(element_time) in [4, 5]):
            word_before_element = string_split[index_time - 1]
            if len(element_time) == 4:
                hour = element_time[:-3]
                minutes = element_time[2:]

            else:
                hour = element_time[:-3]
                minutes = element_time[3:]

            if word_before_element in ['в', 'к']:
                # cprint("в, к", 'yellow')
                mask_str_time = word_before_element + ' ' + element_time
            else:
                mask_str_time = element_time

        else:
            element_time = None


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
