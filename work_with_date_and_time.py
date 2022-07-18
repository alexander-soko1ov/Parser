
import re
from termcolor import colored, cprint
import requests
import datetime
import time

#
# time = datetime.now().time()
#
# print('часов:', time.strftime("%H"))
# print('минут:', time.strftime("%M"))
#
# date = datetime.now()
# print(date.strftime("%A, %d %B, %Y"))

# t1 = "13:00"
#
# t2 = t1.split(":")
#
# print('Часов: ', t2[0])
# print('Минут: ', t2[1])

# import schedule
# def greeting():
#     todos_dict = {
#         '8:00': 'Drink coffee',
#         '11:00': 'Time to work',
#         '23:59': 'Time to sleep'
#     }
#
#     print("Day's tasks")
#     for k, v in todos_dict.items():
#         print(f'{k} - {v}')
#
#     response = requests.get(url='https://yobit.net/api/3/ticker/btc_usd')
#     data = response.json()
#     btc_price = f"BTC: {round(data.get('btc_usd').get('last'), 2)}$"
#     print(btc_price)

# def printing():
#     print("робит")
#
# def main():
#     # greeting()

    # schedule.every(2).seconds.do(printing)
    # schedule.every(5).minutes.do(greeting)

    # schedule.every().day.at('21:09').do(greeting)

    # schedule.every().thursday.do(greeting)
    # time = '21:21'
    # schedule.every().friday.at(time).do(printing)

#     while True:
#         schedule.run_pending()
#
#
# if __name__ == '__main__':
#     main()


# print(globals()['text_' + str(i)])


# import datetime
#
# h = 1
# hour = 20
# minute = 19
#
# today_date = datetime.date.today()
# # date = today_date.strftime("%d.%m.%Y (%A)")
#
# start_time = datetime.timedelta(hours=h)
#
# adding_time = datetime.timedelta(minutes=minute, hours=hour)
#
# time = start_time + adding_time + today_date
#
# time1 = time.strftime("%H:%M")
#
# # print(date)
# # print(start_time)
# # print(adding_time)
# print(time)


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
    message = globals()[f'text_{i}']
    print(message)

    if isinstance(message, str):
        message_split = re.split(' |_', message)
        status = "Success"
    else:
        status = "Failure"
        cprint(status, 'red')
    cprint(message_split, 'green')

    for element in message_split:
        # print(element)
        if element.isdigit():
            # cprint("цифры", 'red')
            datatime = element
            cprint(datatime, 'magenta')
            if (len(element) == 2 or len(element) == 1):
                print('число')
            elif (len(element) == 4):
                print('год')
            else:
                print('ошибка')

        else:
            datatime = None

