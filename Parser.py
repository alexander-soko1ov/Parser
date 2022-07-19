import re
import requests
import datetime
import time
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
test_dict = globals()


for i in range(35):
    message = test_dict[f'text_{i}']
    if isinstance(message, str):
        split_message = list(message.split())
        for index, element in enumerate(split_message):
            if (':' in element) and (element.replace(':', '').isdigit()) and (len(element) in [4, 5]):
                word_before_element = split_message[index - 1]
                if word_before_element in ['в', 'к']:
                    print(word_before_element, element)
                else:
                    print(element)
    cprint(message, 'green')

    def through_time(min=0, hour=0, day=0):
        # min = 30
        current_date = datetime.datetime.today()
        adding_time = datetime.timedelta(minutes=min, hours=hour, days=day)
        time_to_notice = current_date + adding_time
        datatime = time_to_notice.strftime("%d.%m.%Y (%A) %H:%M")
        return datatime

    if message in ['часа', 'часов']:
        result = through_time(hour=h)
    elif message in ['минут', 'минуты']:
        result = through_time(min=m)
    elif message in ['день', 'дней']:
        result = through_time(day=d)
    elif message in ['лет', 'год']:
        result = through_time(day=365)
    else:
        result = through_time()

    # print(colored(result, 'red'))

    status = None
    repeat_always_monday = None
    day_of_week_monday = None
    text = None
    hour = None
    minute = None

    print("MESSAGE=", {'STATUS': status, 'TEXT': text, 'PARAMS': {'repeat_always': repeat_always_monday, 'day_of_week': result}, 'DATE': {'hour': hour, 'minute': minute}})
