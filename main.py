import re
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

    status = None


    # проверка статуса на условия и сплит строки (проблема с пробелами)
    if isinstance(message_space, str):
        message = message_space.lstrip()
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

        # for element_status_str in message_split:
        #     if element_status_str.isdigit() == True:
        #         print("")


    else:
        status = "Failure"

    cprint(message_split, 'green')


    # определение года в числовом формате (2021, 2022) и времени в числовом-текстовом формате (90 минут)
    number = None
    date_number = None
    time = None
    year = None
    mount = None
    mask_str_date = None
    mask_str_time = None
    element_time = None

    dictionary_month = {
        'января': 1,
        'февраля': 2,
        'марта': 3,
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

    dictionary_time = {
        'минут': 1,
        'минуты': 2,
        'часа': 3,
        'часов': 4,
        'число': 5
    }

    recurring_date = {
        'через', 'Через', 'каждые', 'Каждые', 'каждое', 'Каждое', 'каждый', 'Каждый',
        'каждую', 'Каждую'
    }

    days_of_the_week = {
        'понедельник', 'вторник', 'среда', 'четверг', 'пятницу', 'субботу',
        'воскресенье', 'день', 'дня', 'дней', 'неделю', 'недель', 'месяц', 'год',
        'час', 'часа', 'часов'
    }

    for element_1 in message_split:
        if element_1.isdigit():
            if (len(element_1) == 2 or len(element_1) == 1):
                number = element_1
                # print('Число', number)
                index = message_split.index(element_1)
                index_1 = message_split[index + 1]
                index_2 = message_split[index - 1]
                # print(index_2)
                if index_1 in dictionary_month:
                    mount = dictionary_month[index_1]
                    date_number = number
                    mask_str_date = number + " " + index_1
                    # print(number + " " + index_1)
                # elif index_1 in 'число':
                #     date_number = number
                #     mask_str_date = number + " " + index_1
                elif index_2 in recurring_date:
                    if index_1 in dictionary_time:
                        time = number
                        mask_str_time = index_2 + " " + number + " " + index_1

            # elif len(element_1) == 4 and element_1 > '2000':
            #     year = element_1
            #     print(index_2)

            # else:
            #     cprint('Нет даты и времени в текстовом формате', 'red')

    for element_year in message_split:
        # cprint(element_year, 'red')
        if element_year.isdigit() and len(element_year) == 4 and (2000 <= int(element_year) <= 3000):
            year = element_year
            index_element = message_split.index(element_year) + 1
            # print(index_element)
            right_element = message_split[index_element]
            # print(right_element)
            if right_element in ['год', 'года']:
                year = element_year + " " + right_element
                # print(year)
    # print("год:", year)
    element_text_data = None
    each_data = None
    str_each_data = None

    # определение каждый год, каждый день и т.д.
    # cprint(len(message_split), 'red')
    for element_text_data in message_split:
        if element_text_data in recurring_date:
            # cprint(element_text_data, 'magenta')
            index_recurring = message_split.index(element_text_data)
            each_data = str(message_split[index_recurring + 1])
            # cprint(each_data, 'magenta')
            if each_data in days_of_the_week:
                str_each_data = element_text_data + " " + each_data
    # print(str_each_data)

            # if recurring_date in days_of_the_week:
            #     print(element_text_data + " " + recurring_date)

    # определение времени в числовом представлении 16:00, 13:23 и т.д.
    for index_time, element_time in enumerate(message_split):
        # print(element_time)
        if (':' in element_time) and (element_time.replace(':', '').isdigit()) and (len(element_time) in [4, 5]):
            word_before_element = message_split[index_time - 1]
            # cprint(word_before_element, 'red')
            if word_before_element in ['в', 'к']:
                # cprint("в, к", 'yellow')
                mask_str_time = word_before_element + ' ' + element_time
                # cprint(mask_str_time, 'cyan')
            else:
                mask_str_time = element_time
                # cprint(element_time, 'magenta')
        else:
            element_time = None


    # вывод результата, пока что в столбик, для наглядности
    result = ' '.join(message_split)

    print('Статус: ', status)

    if status == "Success":
        print('Число: ', date_number)
        print('Месяц: ', mount)
        print('Год: ', year)
        print('Время: ', mask_str_time)
        print('Datetime (каждый и через):', str_each_data)
        replace_time = result.replace(str(mask_str_time), '')
        replace_date = replace_time.replace(str(mask_str_date), '')
        replace_year = replace_date.replace(str(year), '')
        replace_each_data = replace_year.replace(str(str_each_data), '')
        text = replace_each_data.rstrip().lstrip().capitalize()

        print('Текст: ', text)
    print('\n')

    # print("MESSAGE=",
    #       {'STATUS': status, 'TEXT': text,
    #       'PARAMS': {'repeat_always': repeat_always_monday, 'day_of_week': result},
    #        'DATE': {'hour': hour, 'minute': minute}})