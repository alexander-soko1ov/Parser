import re
from termcolor import colored, cprint
import requests
import datetime
import time


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

    status = None
    text = None
    repeat_always_monday = None
    day_of_week_monday = None
    hour = None
    minute = None
    time_is_given = None

    message = globals()[f'text_{i}']
    cprint(message, 'green')

    if isinstance(message, str):
        message_split = re.split(' |_', message)
        status = "Success"
    else:
        status = "Failure"


    def through_time(min=0, hour=0, day=0, time_is_given=0):
        if time_is_given:
            start_date = datetime.date.today()
            adding_time = datetime.timedelta(minutes=min, hours=hour, days=day)
            time_to_notice = start_date + adding_time
            datatime = time_to_notice.strftime("%d.%m.%Y (%A) %H:%M")
        else:
            current_date = datetime.datetime.today()
            adding_time = datetime.timedelta(minutes=min, hours=hour, days=day)
            time_to_notice = current_date + adding_time
            datatime = time_to_notice.strftime("%d.%m.%Y (%A) %H:%M")

        return datatime

    result = None
    repeat_always_monday = None

    # for element in message_split:
    #     # print(element)
    #     # global result
    #     if element in ["каждый", "каждую", "каждое"]:
    #
    #         for element_data in message_split:
    #             # cprint(element_data, 'red')
    #             if element_data in ['лет', 'год']:
    #                 result = through_time(day=365)
    #             elif element_data in ['часа', 'часов']:
    #                 result = through_time(hour=0)
    #             elif element_data in ['минут', 'минуты']:
    #                 result = through_time(min=0)
    #             elif element_data in ['дней']:
    #                 result = through_time(day=0)
    #             elif 'день' in element_data:
    #                 result = through_time(hour=1)
    #             elif 'день' in element_data:
    #                 result = through_time(day=1)
    #             else:
    #                 result = through_time()

                # repeat_always_monday = data

    # cprint(result, 'magenta')

    cprint(message_split, 'magenta')

    for element in message_split:
        # print(element)
        if "через" in element:
            cprint(element, 'red')
            day_of_week_monday = 'yes'
        if "завтра" in element:
            day_of_week_monday = 'yes'
            cprint(element, 'yellow')

    print("MESSAGE =", {'STATUS': status, 'TEXT': text,
                       'PARAMS': {'repeat_always': repeat_always_monday, 'day_of_week': day_of_week_monday},
                       'DATE': {'hour': hour, 'minute': minute}})