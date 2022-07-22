import re
from termcolor import colored, cprint

# # print('Введите строку:')
# string = 'В понедельник в 21:12'

# string_split = string.split()
# print(string_split)

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


    mount = None
    data = None
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

    # проверка статуса на условия и сплит строки (проблема с пробелами)
    if isinstance(message_space, str):
        message = message_space.lstrip()
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
    else:
        status = "Failure"
        continue

    cprint(string_split, 'green')

    for element in string_split:
        element_on_right = None
        if element in ['каждое', 'каждую', 'каждый']:
            index_element = string_split.index(element) + 1
            element_on_right = string_split[index_element]
            each = element
            index_element_on_rigth = string_split.index(element_on_right)

            if not element_on_right.isdigit() and not (element_on_right in dictionary_datetime):
                day_of_the_week = finding_matches(string_split, days_of_the_week, 1)

            elif element_on_right.isdigit() and ((len(element_on_right) == 1) or (len(element_on_right) == 2)):
                numbers = element_on_right
                index_element_on_rigth = string_split.index(element_on_right)
                month_or_numbers = string_split[index_element_on_rigth + 1]
                cprint('asdafa', 'red')

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
            pass

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
