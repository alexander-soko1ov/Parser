import re
from termcolor import colored, cprint

text_0 = "Начать собираться в 4:31"
text_1 = "Проснуться, улыбнуться, почистить зубы и помыться в 07:13"
text_2 = "Съездить на дачу 17 мая в 16:15"
text_3 = 'Подписать служебку у начальника 13 декабря 2021 года в 16:15'
# text_4 = "Убраться в квартире через 90 минут"
# text_5 = "Позвонить друзьям через 3 часа"
# text_6 = "Приготовить покушать на 2-3 дня 3 сентября 2022 года в 06:01"
# text_7 = "Перевод локального компьютера в режим гибернации завтра"
# text_8 = "Выключить 13 декабря в 20:17"
# text_9 = "Перевод локального компьютера в режим гибернации через 2 дня"
# text_10 = 'Служебку подписать на питон 12 ноября утром'
# text_11 = 'Служебку подписать на питон в четверг в 20:17'
# text_12 = 'Служебку подписать на питон в среду'
# text_13 = 'Служебку в отдел кадров в среду в 13:13'
# text_14 = "В понедельник уроки"
# text_15 = 'Поскольку все записи имеют один и тот же шаблон, внести данные, которые хотите извлечь из пары скобок 13 декабря 2022 года в 16:15'
# text_16 = "Напомни про гречку через 14 минут"
# text_17 = "Через 50 минут таймер установаить. дерзай"
# text_18 = "Основы_Python_в_четверг_15:00 3 сентября 2022 года"
# text_19 = " Основы_Python_в_четверг_15:00 в среду 15:00 "
# text_20 = "13 1311"
# text_21 = 1231
# text_22 = "Сходить покушать на неделе в 13:13"
# text_23 = "del_qustion_answer*как дела?*норма, как сам?"
# text_24 = "Сходить покушать на неделе"
# text_25 = "В следующем месяце Подписать служебку "
# text_26 = "\d\de23 2\3 3r3556"
# text_27 = "Подписать служебку по выходным"
# text_28 = "Сходить в сауну каждое 28 число"
# text_29 = "Подписать служебку по выходным в 20:19"
# text_30 = "поздравить с др маму через год в 20:18"
# text_31 = "поздравить с др маму через час"
# text_32 = "тренировка каждый час в 20:19"
# text_33 = "Подписать служебку 23 февраля"
# text_34 = "Тренировка каждый понедельник"
# text_35 = "Тренировка каждый день"

for i in range(4):
    message = globals()[f'text_{i}']
    print(message)

    if isinstance(message, str):
        message_split = re.split(' |_', message)
        status = "Success"
    else:
        status = "Failure"
        cprint(status, 'red')
        continue
    cprint(message_split, 'green')

    dictionary = {
        'января': 'January',
        'февраля': 'February',
        'марта': 'March',
        'апреля': 'April',
        'мая': 'May',
        'июня': 'June',
        'июля': 'July',
        'августа': 'August',
        'сентября': 'September',
        'октября': 'October',
        'ноября': 'November',
        'декабря': 'December'
    }
    number = None
    year = None
    mask_str_date = None

    for element in message_split:
        # print(element)
        if element.isdigit():
            if (len(element) == 2 or len(element) == 1):
                number = element
                # print('Число', number)
                index = message_split.index(element)
                index_1 = message_split[index+1]
                if index_1 in dictionary:
                    mount = dictionary[index_1]
                    mask_str_date = number + " " + index_1
                elif index_1 in 'число':
                    mask_str_date = number + " " + index_1

            elif len(element) == 4 and element > '2000':
                year = element

            else:
                p = 'ошибка'

    result = ' '.join(message_split)
    print('Число: ', mask_str_date)
    print('Год: ', year)
    print(result)

    text = None

    for split_word in [mask_str_date, year]:
        # print(split_word)
        if (mask_str_date == None or year == None):
            text = "нет"# print("123")
        else:
            text = "".join(message.split(split_word))

    print('Текст:', text)
        # text = result.lstrip().capitalize()