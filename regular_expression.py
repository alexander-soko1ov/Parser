import re
from datetime import datetime
from termcolor import cprint

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

# for i in range(36):
#     # print(globals()['text_' + str(i)])
#     message = globals()[f'text_{i}']
#     print(message)

print("О чем мне вам напомнить?")
message = input()

# text1 = re.findall(r'[а-яА-ЯёЁ]', message)
# text2 = ' '.join(text1)
# text3 = re.sub(r'[вВ][\s][0-9]?[0-9][:][0-9][0-9]+', '', text2)
# text = re.sub(r'завтра|[вВ] понедельник|[вВ][о]? вторник|[вВ] среду|[вВ] четверг|[вВ] пятницу|[вВ] субб?оту|[вВ] воскресенье', '', text3)

# print(text)

time_ = re.findall('[0-9]?[0-9][:][0-9][0-9]', message)

string = list(message.split())

time_str = ''.join(time_)

t = time_str.split(":")

hour = t[0]
minute = t[1]

print('HOUR: ', hour)
print('MINUTE: ', minute)

word_before_time = string[string.index(time_str) - 1]
list_check_word_before_time = ['в', 'к', 'на']

for word in list_check_word_before_time:
    if word == word_before_time:
        time_str = f'{word} {time_str}'

message = ''.join(message.split(time_str))

print(message)

date = re.findall("[0-9]?[0-9][.,-]?[0-1]?[1-9]?[.,-]?[0-9]?[0-9]?[0-9]?[0-9]?", message)
date_str = ''.join(date)
if date_str == '':
    date_str = None
# message = ''.join(message.split(date))
print('DATE: ', date_str)


day1 = re.findall(r"завтра|[вВ] понедельник|[вВ][о]? вторник|[вВ] среду|[вВ] четверг|[вВ] пятницу|[вВ] субб?оту|[вВ] воскресенье", message)
day_str = ''.join(day1)
if day_str == '':
    day_str = None
print('DAY: ', day_str)

# print(cprint())

status = None
repeat_always_monday = None
day_of_week_monday = None

string = message
for split_word in [day_str, date_str, time_str]:
    string = ' '.join(string.split(split_word))
    string = string.rstrip()

if "каждый" or "каждую" or "каждое" in message:
    repeat_always_monday = day_str
else:
    day_of_week_monday = day_str

print('TEXT: ', string)

print("MESSAGE=", {'STATUS': status, 'TEXT': string,
                   'PARAMS': {'repeat_always': repeat_always_monday,
                              'day_of_week': day_of_week_monday},
                   'DATE': {'hour': hour, 'minute': minute}})

# сходить в магаз в субботу 26.02 в 13:56

# поработать с тем, что когда убираешь время из сообщения, то всё ломается