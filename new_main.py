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

for i in range(36):
    message_space = globals()[f'text_{i}']
    print(message_space)

    """объявление и обнуление глобальных переменных"""
    status = None
    time = None
    each = None
    numbers = 0
    hour = 0
    minutes = 0
    weeks = 0
    day_of_the_week = 0
    mount = 0
    datetime_element = None

    text = 'None'

    """добавление словарей для работы с текстом"""
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
        'дня': 3,
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
        работает с предлогами, возвращает:
            0 - значение из текста
            1 - значение ключа из словаря"""
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


    def removal_of_excess(message_del, message, message_split, element_del):
        """удаление лишних элементов из текста"""
        if not element_del == '':
            if element_del in message_split:
                final_text = ' '.join(message.split()[:message.split().index(element_del)])
            else:
                final_text = message_del
        else:
            final_text = message_del
        return final_text


    """время и дата сейчас"""
    datetime_today = datetime.datetime.today()
    weekday = datetime_today.weekday()
    minute = datetime_today.minute
    hour = datetime_today.hour
    day = datetime_today.day
    mount = datetime_today.month
    year = datetime_today.year

    """проверка статуса на условия и сплит строки (проблема с пробелами)"""
    if isinstance(message_space, str):
        message = message_space.lstrip().lower()
        message_split = re.split(' ', message)
        status = None
        # print(message_split[0])

        for element_status_word in message_split[0]:
            # cprint(element_status_word, 'red')
            if element_status_word in ['/', '\\', 'd']:
                status = "Failure"
                break
            elif " " in element_status_word:
                status = "Success"
            else:
                status = "Success"
        cprint(message_split, 'green')


    else:
        status = "Failure"
        message_space = ''

    """определение времени в формате 12:17, 0:12 и т.д."""

    time = re.findall(r'[\s][0-9]?[0-9][:][0-9][0-9]', message_space)

    # mask_time = ''.join(re.findall(r'[\s]?[нН]?[вВаА]?[\s][0-9]?[0-9][:][0-9][0-9]', message_space))

    if not time == []:
        time_res = time
        time_str = ''.join(time_res).lstrip()
        if len(time_str) == 4:
            hour = time_str[:1]
            minute = time_str[2:]
        elif len(time_str) == 5:
            hour = time_str[:2]
            minute = time_str[3:]

    """проверка на месяц, проверка на слово 'число', слова 'минут, часов и т.д."""
    for element_date in message_split:

        """проверка элемент является цифрой или нет, и что стоит после элемента, 
        если он является цифрой"""
        if element_date.isdigit() and (len(element_date) == 1 or len(element_date) == 2):
            index_element_right = message_split.index(element_date) + 1

            if not finding_matches(message_split, dictionary_month, 1) == None:    # проверка на месяц
                day = element_date
                mount = finding_matches(message_split, dictionary_month, 1)
                mount_text = finding_matches(message_split, dictionary_month, 2)
            elif message_split[index_element_right] in ['число']:   # проверка на слово 'число'
                mount = datetime_today.month
            elif not finding_matches(message_split, dictionary_datetime, 1) == None:    # проверка на слова 'минут, часов и т.д.'
                # cprint(finding_matches(message_split, dictionary_datetime, 2), 'red')
                if finding_matches(message_split, dictionary_datetime, 1) == 1:
                    # минут
                    datetime_minutes = datetime_today + datetime.timedelta(minutes=int(element_date))
                    hour = datetime_minutes.hour
                    minute = datetime_minutes.minute
                    day = datetime_minutes.day
                elif finding_matches(message_split, dictionary_datetime, 1) == 2:
                    # часов
                    datetime_minutes = datetime_today + datetime.timedelta(hours=int(element_date))
                    hour = datetime_minutes.hour
                    day = datetime_minutes.day
                    mount = datetime_minutes.month
                elif finding_matches(message_split, dictionary_datetime, 1) == 3:
                    # дней
                    datetime_minutes = datetime_today + datetime.timedelta(days=int(element_date))
                    day = datetime_minutes.day
                    mount = datetime_minutes.month
                elif finding_matches(message_split, dictionary_datetime, 1) == 4:
                    # недель
                    datetime_minutes = datetime_today + datetime.timedelta(weeks=int(element_date))
                    day = datetime_minutes.day
                    mount = datetime_minutes.month

        elif element_date in ['год', 'года', 'лет']:
            """проверка на слова 'год', 'года', 'лет' и проверка високосный ли сейчас год,
             прибавление кол-ва лет к нынешнему году"""
            element_message_split_left = message_split[message_split.index(element_date) - 1]
            if element_message_split_left.isdigit():
                day_multiplier = int(element_message_split_left)
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


    for element_pronoun in message_split:
        if element_pronoun in ['каждый', 'каждую', 'каждое', 'каждые']:
            # print(element_pronoun)
            cprint(message_split.index(element_pronoun), 'magenta')
            each_key = 3
            each = element_pronoun
            # записать время в переменную повторения в выводе, в формате json
        elif element_pronoun in ['через']:
            element_right_eash = message_split[message_split.index(element_pronoun) + 1]
            cprint(element_right_eash, 'red')
            each_key = 2
            each = element_pronoun
            # просто прибавить время

    # if (suggestion_function(message_split, prefix_dictionary, 1) == 3) or (suggestion_function(message_split, prefix_dictionary, 1) == 2):
    #     cprint(suggestion_function(message_split, prefix_dictionary, 1), 'red')
    #     # each = suggestion_function(message_split, prefix_dictionary, 0)
    #     cprint('каждый или через', 'red')
        # if (suggestion_function(message_split, prefix_dictionary, 1) == 2) or (suggestion_function(message_split, prefix_dictionary, 1) == 3):
        #
        #     index_element_right_eash = message_split.index(each) + 1
        #     # element_right_eash = message_split[index_element_right_eash]
        #     cprint(len(message_split), 'cyan')
        #     cprint(index_element_right_eash, 'magenta')
    # else:
    #     eash = None

    """!!!скорее всего буду делать в кажом блоке отдельное прибавление времени!!!
    работа с datetime, получение года, месяца, даты и времени, исходя из изначальных условий"""
    # number = datetime_today + datetime.timedelta(minutes=int(minutes), hours=int(hour), days=int(day), weeks=int(weeks))
    # year = number.year
    # mount = number.month
    # day = number.day
    # hour = number.hour
    # minutes = number.minute
    # weekday = number.weekday()

    """вывод данных для отладки"""
    print('статус: ', status)
    # print('Время: ', time)

    if status == 'Success':
        print('предлог: ', each)
        print('число: ', day)
        print('часы: ', hour)
        print('минуты: ', minute)
        print('год: ', year)
        print('день недели: ', weekday)
        print('месяц: ', mount)
        print('час, месяц, год и.д.: ', datetime_element)
        # print('на: ', on_the_week)

        """вывод масок для удаления из текста"""

        # print('маска времени: ', message_split.index(str(' '.join(time).lstrip())))


        """вывод итогового текста"""
        # del_time = removal_of_excess(message_space, message_space, message_split, str(' '.join(time).lstrip()))
        # print(removal_of_excess(del_time, message_space, message_split, day))


        # text_result = ' '.join(re.split(' |_', message_space)).lstrip().capitalize()
        # print('итоговый текст: ', text_result)
    print('\n')