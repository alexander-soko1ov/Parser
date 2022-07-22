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
text_35 = "Тренировка каждый год"

string = 'в понедельник'
string_split = string.lower().split()
print(string_split)

days_of_week_dict = {
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
    'минута': 1,
    'час': 2,
    'день': 3,
    'неделя': 4,
    # 'месяц': 5,
    # 'год': 6
}

prefix_dictionary = {
    'в': 1,
    'через': 2,
    'кажд': 3
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


'''
время и дата сейчас
'''
datetime_today = datetime.datetime.today()
weekday_today = datetime_today.weekday()
# date_difference = 0
mask_time = None
mask_data = None
day_of_week = None
prefixes = None
# weeks = 0
day = datetime_today.day
mount = datetime_today.month
year = datetime_today.year
# weekday = 0
# hour = 0
# minutes = 0
mask_every = None


'''
определение предлогов 'в, через и тд.' и дней недели
'''
if finding_matches(string_split, prefix_dictionary, 1) == 1:
    prefixes = finding_matches(string_split, prefix_dictionary, 0)
    # print(prefixes)
    # mask_data = prefixes + ' ' + finding_matches(string_split, days_of_the_week, 2)
    # print(finding_matches(string_split, days_of_the_week, 2))

""" модуль работает с датами в формате 'каждый день, через день, через неделю и т.д.' """
datetime_today = datetime.datetime.today()
# print(datetime_today)
minute_every = 0
hour_every = 0
day_every = 0
weeks_every = 0
mask_every = None

# print(suggestion_function(string_split, prefix_dictionary, 1))
if (suggestion_function(string_split, prefix_dictionary, 1) == 2) or (suggestion_function(string_split, prefix_dictionary, 1) == 3):
    index_element_right = string_split.index(suggestion_function(string_split, prefix_dictionary)) + 1
    # print(finding_matches(string_split, dictionary_datetime, 1))
    if finding_matches(string_split, dictionary_datetime, 1) == 1:
        minute = 1
    elif finding_matches(string_split, dictionary_datetime, 1) == 2:
        hour = 1
    elif finding_matches(string_split, dictionary_datetime, 1) == 3:
        day = 1
    elif finding_matches(string_split, dictionary_datetime, 1) == 4:
        weeks = 7


'''
определение дней недели 
'''
for day_of_week in string_split:
    # определение дней недели
    date_def = finding_matches(string_split, days_of_week_dict, 1)

    if date_def in [0, 1, 2, 3, 4, 5, 6]:
        day_of_week = get_key_by_value(date_def, days_of_week_dict)
        if days_of_week_dict[day_of_week] < weekday_today:
            minute_every = days_of_week_dict[day_of_week] - weekday_today + 7
        elif days_of_week_dict[day_of_week] == weekday_today:
            minute_every = days_of_week_dict[day_of_week] - weekday_today + 7
        elif days_of_week_dict[day_of_week] > weekday_today:
            minute_every = days_of_week_dict[day_of_week] - weekday_today
    else:
        day_of_week = get_key_by_value(weekday_today, days_of_week_dict)

'''
вывод из общей даты и времени отдельных составляющих даты и времени
'''
# number = datetime_today + datetime.timedelta(days=date_difference, weeks=weeks)
number = datetime_today + datetime.timedelta(minutes=minute_every, hours=hour_every, days=day_every, weeks=weeks_every)
ear = number.year
year = number.year
mount = number.month
day = number.day
# print(date_difference)
hour = number.hour
minutes = number.minute
weekday = number.weekday()


if not suggestion_function(string_split, prefix_dictionary, 0) == None and not finding_matches(string_split, dictionary_datetime, 0) == None:
    mask_every = suggestion_function(string_split, prefix_dictionary, 0) + " " + finding_matches(string_split, dictionary_datetime, 2)



    """определение времени в формате 12:17, 0:12 и т.д."""

    time = re.findall(r'[\s][0-9]?[0-9][:][0-9][0-9]', string)

    mask_time = ''.join(re.findall(r'[\s]?[нН]?[вВаА]?[\s][0-9]?[0-9][:][0-9][0-9]', string))

    if not time == []:
        time_res = time

        time_str = ''.join(time_res).lstrip()

        if len(time_str) == 4:
            hour = time_str[:1]
            minutes = time_str[2:]
        elif len(time_str) == 5:
            hour = time_str[:2]
            minutes = time_str[3:]
        # mask_time = ' ' + hour + ":" + minutes




'''
вывод данный для удобной отладки программы
'''
print(day, mount, year)
print('приставка: ', prefixes)
print('день недели: ', day_of_week)
print('число: ', day)
print('часы: ', hour)
print('минуты: ', minutes)

'''
маски для replace
'''

# print('маска времени: ', mask_time)
if not finding_matches(string_split, days_of_week_dict, 2) == None:
    print('маска дней недели: ', prefixes + ' ' + str(finding_matches(string_split, days_of_week_dict, 2)))


# if mask_time == None:
#     if not mask_data == None:
#         text = string.replace(mask_data, '')
#     else:
#         text = string
# else:
#     if not mask_data == None:
#         text_not_time = string.replace(mask_time, '')
#         text = text_not_time.replace(mask_data, '')
#     else:
#         text = string.replace(mask_time, '')
#
# if not mask_every == None:
#     print('маска каждый день и тд.: ', mask_every)
#     text = string.replace(mask_every, '')

'''
вывод итогового текста
'''
# print('текст: ', text)
#
# text_result = ' '.join(re.split(' |_', text))
# print('итоговый текст: ', text_result)