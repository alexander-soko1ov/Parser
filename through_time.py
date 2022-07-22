import datetime
from termcolor import colored, cprint

string = 'Тренировка через 3 дня'
string_split = string.lower().split()
print(string_split)

prefix_dictionary = {
    'в': 1,
    'через': 2,
    'кажд': 3
}

dictionary_datetime = {
    'минута': 1,
    'час': 2,
    'день': 3,
    'дня': 3,
    'дней': 3,
    'неделя': 4,
    # 'месяц': 5,
    # 'год': 6
}

def get_key_by_value(value, dictionary):
    """возвращет ключ по значению из словаря"""
    result_key = None
    for element in dictionary:
        if dictionary[element] == value:
            result_key = element
    return result_key


def suggestion_function(string_split, dictionary, number=0):
    """возвращает значение или элемент словаря подходящий к строке,
    работает с предлогами"""
    result = None
    pre_result = None
    pre_result_text = None
    for element in string_split:
        for element_dict in dictionary:
            if len(element) == 6:
                element_for_comparison = element[:-2]
                if element_for_comparison in element_dict:
                    pre_result_text = element
                    pre_result = prefix_dictionary[element_dict]
            elif len(element) == 7:
                element_for_comparison = element[:-3]
                if element_for_comparison in element_dict:
                    pre_result_text = element
                    pre_result = prefix_dictionary[element_dict]
            elif element in element_dict:
                pre_result = prefix_dictionary[element_dict]
                pre_result_text = element
    if number == 1:
        """вывод значения ключа из словаря"""
        result = pre_result
    elif number == 0:
        """вывод значения из текста"""
        result = pre_result_text
    else:
        result = None

    return result

def finding_matches(string_split, dictionary, text=0):
    """определяет дни недели, месяцы и другое, отбрасывая окончания,
    возвращает:
        0 - тектовый элемент словаря
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

def through_time(string_split, dictionary, format_date=0, mask=0):
    """функция работает с датами в формате 'каждый день, через день, через неделю и т.д.' """

    datetime_today = datetime.datetime.today()
    minute = 0
    hour = 0
    day = 0
    weeks = 0
    mask_every = None
    mask_time = None

    if (suggestion_function(string_split, dictionary, 1) == 2) or (suggestion_function(string_split, dictionary, 1) == 3):
        element_right = string_split[string_split.index(suggestion_function(string_split, dictionary)) + 1]
        if element_right.isdigit() and len(str(element_right)) in [1, 2]:
            minute = int(element_right)

        if finding_matches(string_split, dictionary_datetime, 1) == 1:
            minute = 1
            if element_right.isdigit() and len(str(element_right)) in [1, 2]:
                minute = int(element_right)
                mask_time = element_right
        elif finding_matches(string_split, dictionary_datetime, 1) == 2:
            hour = 1
            if element_right.isdigit() and len(str(element_right)) in [1, 2]:
                hour = int(element_right)
                mask_time = element_right
        elif finding_matches(string_split, dictionary_datetime, 1) == 3:
            day = 1
            if element_right.isdigit() and len(str(element_right)) in [1, 2]:
                day = int(element_right)
                mask_time = element_right
        elif finding_matches(string_split, dictionary_datetime, 1) == 4:
            weeks = 7
            if element_right.isdigit() and len(str(element_right)) in [1, 2]:
                weeks = int(element_right)
                mask_time = element_right
    number = datetime_today + datetime.timedelta(minutes=minute, hours=hour, days=day, weeks=weeks)
    day = number.day
    mount = number.month
    year = number.year
    hour = number.hour
    minute = number.minute
    pre_result = [day, mount, year, hour, minute]

    if not suggestion_function(string_split, dictionary, 0) == None and not finding_matches(string_split, dictionary_datetime, 0) == None and not mask_time == None:
        mask_every = suggestion_function(string_split, dictionary, 0) + " " + mask_time + " " + finding_matches(string_split, dictionary_datetime, 2)
    elif mask_time == None:
        mask_every = suggestion_function(string_split, dictionary, 0) + " " + finding_matches(string_split, dictionary_datetime, 2)

    if format_date == 0:
        result = number
    elif format_date == 1:
        result = pre_result
    if mask == 1:
        result = mask_every

    return result

print('формат дата:', through_time(string_split, prefix_dictionary, 1))
print('дата: ', through_time(string_split, prefix_dictionary))
print('маска: ', through_time(string_split, prefix_dictionary, 0, 1))