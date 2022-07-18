# import datetime
#
# text_0 = "Начать собираться в 4:31"
# text_1 = "Проснуться, улыбнуться, почистить зубы и помыться в 07:13"
# text_2 = "Съездить на дачу 17 мая в 16:15"
# text_3 = 'Подписать служебку у начальника 13 декабря 2021 года в 16:15'
# text_4 = "Убраться в квартире через 90 минут"
# text_5 = "Позвонить друзьям через 3 часа"
# text_6 = "Приготовить покушать на 2-3 дня"
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
#
# time_today = datetime.datetime.today()
# # print(time_today)
#
# year = time_today.year
# mount = time_today.month
# day = time_today.day
# hour = 0
# minute = 90
#
# after_time = datetime.datetime(year=year, month=mount, day=day)
#
# delta_time = datetime.timedelta(hours=hour, minutes=minute)
#
# through_time = time_today + delta_time
#
# at_the_time = after_time + delta_time
#
#
# print('через время ', through_time)
# print('в назначенное время ', at_the_time)

string = "2021 года"

string_split = string.split()
print(string_split)

data = None

for element in string_split:
    if element.isdigit() and len(element) == 4:
        data = element
        index_element = element.index(element)+1
        # print(index_element)
        right_element = string_split[index_element]
        if right_element in ['год', 'года']:
            data = element + " " + right_element
print("год:", data)