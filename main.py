import random
from termcolor import colored, cprint
import datetime
import re

from termcolor import cprint, colored


SUCCESS = "SUCCESS"
FAILED = "FAILED"


def regex_or(lst: list):
    lst = ["(" + el + ")" for el in lst]
    res = f"({'|'.join(lst)})"
    return res


def regex_or_var(lst: list, var_name: str):
    lst = ["(" + el + ")" for el in lst]
    res = f"(?P<{var_name}>{'|'.join(lst)})"
    return res


def var(txt: str, var_name: str):
    res = f"(?P<{var_name}>{txt})"
    return res


def find_dict_match(exact_value: str, map_dict: dict):
    """функция получения ключа из словаря по его значению"""
    for key, regex_value in map_dict.items():
        m = re.search(regex_value, exact_value)
        if m:
            return key
    return None


def parse_message(message: str):
    res = {}
    matches = []
    for pattern in patterns:
        m = re.search(pattern, message.lower())
        if m:
            matches.append(m)
            res.update(m.groupdict())

    return res, matches


def highlight_message(message: str, matches: list, **print_kwargs):
    if not matches:
        cprint(message, 'red', **print_kwargs)
        return
    matches.sort(key=lambda x: x.start())
    colored_msg = ''
    first, last = matches[0], matches[-1]
    colored_msg += colored(message[0:first.start()], 'red')
    for i, match in enumerate(matches):
        colored_msg += colored(message[match.start():match.end()], 'green')
        if match is not last:
            colored_msg += colored(message[match.end():matches[i+1].start()], 'red')
    colored_msg += colored(message[last.end():len(message)], 'red')
    print(colored_msg, **print_kwargs)


def get_task(message: str, matches: list):
    if not matches:
        return None
    matches.sort(key=lambda x: x.start())
    task_list = []
    first, last = matches[0], matches[-1]

    task_list.append(message[0:first.start()].strip()) if message[0:first.start()].strip() else None
    for i, match in enumerate(matches):
        if match is not last:
            task_list.append(message[match.end():matches[i + 1].start()].strip()) if message[match.end():matches[i + 1].start()].strip() else None

    task_list.append(message[last.end():len(message)].strip()) if message[last.end():len(message)].strip() else None
    if not task_list:
        return None
    else:
        return ' '.join(task_list)


relative_days = ["сегодня", "завтра", "послезавтра"]
part_of_day = ["(с )?утра?(ом)?", "дн[её]м", "вечером", "ночью"]
every = ["кажд[ыоу][йею]", "по"]
days_of_weeks = {
    0: "понедельник(ам)?",
    1: "вторник(ам)?",
    2: "среду?(ам)?",
    3: "четверг(ам)?",
    4: "пятницу?(ам)?",
    5: "субботу?(ам)?",
    6: "воскресенье?(ям)?"
}
months = {
    0: "числа",
    1: "январ[ья]",
    2: "феврал[ья]",
    3: "март[а]?",
    4: "апрел[ья]",
    5: "ма[йя]",
    6: "июн[ья]",
    7: "июл[ья]",
    8: "август[а]?",
    9: "сентябр[ья]",
    10: "октябр[ья]",
    11: "ноябр[ья]",
    12: "декабр[ья]",
}
time_measure = dict(
    years=regex_or(["год[ау]?", "лет"]),
    months="месяц[ае]?",
    weeks="недел[юие]",
    days="де?н[яье][й]?",
    hours="час[а]?(ов)?",
    minutes="минут[уы]?",
    # seconds="секунд[уы]?",
    day='числ[оа]',
    days_of_weeks=regex_or(list(days_of_weeks.values())),
    weekend='выходны[емх]'
)
all_dct = list(time_measure.values())

# PATTERNS
year_pattern = f'{var("[2-3][0-1][0-9][0-9]", "year")} (года?)?'
day_week_pattern = f'в {regex_or_var(list(days_of_weeks.values()), "days_of_week")}'
day_pattern = f'{var("[0-9]{1,2}", "day")} {regex_or_var(list(months.values()), "month")}'
time_pattern = 'в? (?P<hours>\d{1,2}):(?P<minutes>\d{2})'

every_pattern = f'{regex_or_var(every, "every")} (?P<amount>\d*)\s?{regex_or_var(all_dct, "time_range")}'
after_pattern = f'{var("через", "after")} (?P<amount>\d*)\s?{regex_or_var(all_dct, "time_range")}'

relative_pattern = f"{regex_or_var(relative_days, 'relative')}"
part_of_day_pattern = f"{regex_or_var(part_of_day, 'part_of_day')}"

on_pattern = 'на\s(?P<week_weekend>(неделе)|(выходны[хм]))'
on_next_pattern = f'{regex_or(["на", "в"])} следующ[ие][йм] {regex_or_var(list(time_measure.values()), "next")}'

patterns = [time_pattern, every_pattern, day_week_pattern, day_pattern, year_pattern, relative_pattern,
            part_of_day_pattern, on_pattern, on_next_pattern, after_pattern]


with open('dataset.txt', encoding='utf-8') as file:
    dataset = file.read().splitlines()


def relative_def(res, json_output):
    """функция обработки СЕГОДНЯ, ЗАВТРА, ПОСЛЕЗАВТРА"""
    relative = res['relative']
    if relative == 'завтра':
        day_add = 1
    elif relative == 'послезавтра':
        day_add = 2
    else:
        day_add = 0
    datetime_after = now + datetime.timedelta(days=day_add)
    day = datetime_after.day
    month = datetime_after.month

    json_output['DATE']['day'] = day
    json_output['DATE']['month'] = month


def week_weekend_def(res, json_output):
    """функция обработки НА ВЫХОДНЫХ, НА НЕДЕЛЕ"""
    weekday_rand = None
    day_every = None
    weekday = datetime.datetime.now().weekday()

    if res['week_weekend'] == 'неделе':
        if weekday == 4:
            weekday_rand = random.randint(0, 4)
        else:
            if weekday == 6:
                number_one = 0
            else:
                number_one = weekday + 1
            weekday_rand = random.randint(number_one, 4)
    elif (res['week_weekend'] == 'выходным') or (res['week_weekend'] == 'выходных'):
        weekday_rand = random.randint(5, 6)

    if weekday_rand < int(weekday):
        day_every = weekday_rand - weekday + 7
    elif weekday_rand == weekday:
        day_every = 7
    elif weekday_rand > weekday:
        if weekday == 5:
            day_every = 5 - weekday + random.randint(6, 7)
        else:
            day_every = weekday_rand - weekday

    number = now + datetime.timedelta(days=day_every)
    day = number.day
    month = number.month
    year = number.year
    json_output['DATE']['day'] = day
    json_output['DATE']['month'] = month
    json_output['DATE']['year'] = year


def through_time_def(res, now, json_output):
    """через время"""

    if ('after' in res) or ('every' in res):
        # repeat_after = res["after"] + ' ' + res["amount"] + ' ' + res["time_range"]
        if res["amount"] == '':
            if 'every' in res:
                res["amount"] = 1
                json_output['PARAMS']['repeat_every'] = res["every"] + ' ' + res["time_range"]
            elif 'after' in res:
                res["amount"] = 1

        if find_dict_match(res["time_range"], time_measure) == 'minutes':
            datetime_after = now + datetime.timedelta(minutes=int(res["amount"]))
            json_output['DATE']['minute'] = datetime_after.minute
            json_output['DATE']['hour'] = datetime_after.hour
            if 'every' in res:
                json_output['PARAMS']['repeat_every'] = res["every"] + ' ' + str(res["amount"]) + ' ' + res["time_range"]

        elif find_dict_match(res["time_range"], time_measure) == 'hours':
            datetime_after = now + datetime.timedelta(hours=int(res["amount"]))
            json_output['DATE']['hour'] = datetime_after.hour
            if 'every' in res:
                json_output['PARAMS']['repeat_every'] = res["every"] + ' ' + str(res["amount"]) + ' ' + res["time_range"]

        elif find_dict_match(res["time_range"], time_measure) == 'days':
            datetime_after = now + datetime.timedelta(days=int(res["amount"]))
            json_output['DATE']['day'] = datetime_after.day
            json_output['DATE']['month'] = datetime_after.month
            if 'every' in res:
                json_output['PARAMS']['repeat_every'] = res["every"] + ' ' + str(res["amount"]) + ' ' + res["time_range"]

        elif find_dict_match(res["time_range"], time_measure) == 'weeks':
            datetime_after = now + datetime.timedelta(weeks=int(res["amount"]))
            json_output['DATE']['day'] = datetime_after.day
            json_output['DATE']['month'] = datetime_after.month
            if 'every' in res:
                json_output['PARAMS']['repeat_every'] = res["every"] + ' ' + str(res["amount"]) + ' ' + res["time_range"]

        elif find_dict_match(res["time_range"], time_measure) == 'months':
            datetime_after = now + datetime.timedelta(days=30 * int(res["amount"]))
            json_output['DATE']['day'] = datetime_after.day
            json_output['DATE']['month'] = datetime_after.month
            if 'every' in res:
                json_output['PARAMS']['repeat_every'] = res["every"] + ' ' + str(res["amount"]) + ' ' + res["time_range"]

        elif find_dict_match(res["time_range"], time_measure) == 'years':
            json_output['DATE']['year'] += int(res["amount"])
            if 'every' in res:
                json_output['PARAMS']['repeat_every'] = res["every"] + ' ' + str(res["amount"]) + ' ' + res["time_range"]



def main_handler(message):
    """главная функция обработки данных полученных парсером"""
    res, matches = parse_message(message)

    # ПОЛУЧЕНИЕ ИТОГОВОГО ТЕКСТА
    task = str(get_task(message, matches)).strip().capitalize()

    # ОПРЕДЕЛЕНИЕ СТАТУСА
    status = SUCCESS
    if task is None:
        status = FAILED
        json_output = 'Status: FAILED'
    else:
        repeat_every = None

        # ВРЕМЯ СЕЙЧАС
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute
        day = now.day
        month = now.month
        year = now.year

        # ИТОГОВЫЙ ВЫВОД
        json_output = {'STATUS': status, 'TEXT': task,
                       'PARAMS': {'repeat_every': repeat_every},
                       'DATE': {'hour': hour, 'minute': minute, 'day': day, 'month': month, 'year': year}}

        # СЕГОДНЯ, ЗАВТРА, ПОСЛЕЗАВТРА
        if 'relative' in res:
            relative_def(res, json_output)

        # ВРЕМЯ В ЦИФРОВОМ ФОРМАТЕ
        if ('hours' and 'minutes') in res:
            json_output['DATE']['hour'] = res['hours']
            json_output['DATE']['minute'] = res['minutes']

        # ЧИСЛО + МЕСЯЦ
        if 'month' in res:
            json_output['DATE']['month'] = find_dict_match(res["month"], months)
            json_output['DATE']['day'] = res['day']

        # НА ВЫХОДНЫХ, НА НЕДЕЛЕ
        if ('week_weekend' or 'time_range') in res:
            week_weekend_def(res, json_output)

        # ЧЕРЕЗ ВРЕМЯ / КАЖДОЕ ВРЕМЯ
        if ('after' in res) or ('every' in res):
            through_time_def(res, now, json_output)

        # КАЖДОЕ ВРЕМЯ
        if 'every' in res:
            pass
            # every_time_def(res, json_output)

    return json_output


for message in dataset:

    res, matches = parse_message(message)
    task = get_task(message, matches)
    status = SUCCESS
    if task is None:
        status = FAILED

    highlight_message(message, matches, end=' ')

    print(res, task)
    print("MESSAGE =", main_handler(message))

    now = datetime.datetime.now()
    text = task
    repeat = None
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    weekday = now.weekday()




    # # ВРЕМЯ В ЦИФРОВОМ ФОРМАТЕ
    # if ('hours' and 'minutes') in res:
    #     hour = res['hours']
    #     minute = res['minutes']
    #
    # # ЧИСЛО + МЕСЯЦ
    # if 'month' in res:
    #     month = find_dict_match(res["month"], months)
    #     day = res['day']

    # НА ВЫХОДНЫХ, НА НЕДЕЛЕ
    # weekday_rand = None
    # day_every = None
    # if ('week_weekend' or 'time_range') in res:
    #     if (res['week_weekend'] == 'неделе') or (res['week_weekend'] == 'выходным') or (res['week_weekend'] == 'выходных'):
    #         if weekday == 4:
    #             weekday_rand = random.randint(0, 4)
    #         else:
    #             if weekday == 6:
    #                 number_one = 0
    #             else:
    #                 number_one = weekday + 1
    #             weekday_rand = random.randint(number_one, 4)
    #     else:
    #         weekday_rand = random.randint(5, 6)
    #     if weekday_rand < int(weekday):
    #         day_every = weekday_rand - weekday + 7
    #     elif weekday_rand == weekday:
    #         day_every = 7
    #     elif weekday_rand > weekday:
    #         if weekday == 5:
    #             day_every = 5 - weekday + random.randint(6, 7)
    #         else:
    #             day_every = weekday_rand - weekday
    #     number = now + datetime.timedelta(days=day_every)
    #     day = number.day
    #     month = number.month
    #     year = number.year

    # ДЕНЬ НЕДЕЛИ




    # ЧЕРЕЗ ВРЕМЯ

# def through_time_def(res, now):
#     repeat_after = None
#     repeat_every = None
#     # через время
#     # if 'after' in res and res["amount"] == '':
#     #     repeat_after = res["after"] + ' ' + res["time_range"]
#     if 'after' in res:
#         repeat_after = res["after"] + ' ' + res["amount"] + ' ' + res["time_range"]
#         if res["amount"] == '':
#             res["amount"] = 1
#         else:
#             pass
#
#         if find_dict_match(res["time_range"], time_measure) == 'minutes':
#             datetime_after = now + datetime.timedelta(minutes=int(res["amount"]))
#             minute = datetime_after.minute
#             hour = datetime_after.hour
#
#         elif find_dict_match(res["time_range"], time_measure) == 'hours':
#             datetime_after = now + datetime.timedelta(hours=int(res["amount"]))
#             hour = datetime_after.hour
#
#         elif find_dict_match(res["time_range"], time_measure) == 'days':
#             datetime_after = now + datetime.timedelta(days=int(res["amount"]))
#             day = datetime_after.day
#
#         elif find_dict_match(res["time_range"], time_measure) == 'weeks':
#             datetime_after = now + datetime.timedelta(weeks=int(res["amount"]))
#             day = datetime_after.day
#             month = datetime_after.month
#
#         elif find_dict_match(res["time_range"], time_measure) == 'months':
#             datetime_after = now + datetime.timedelta(days=30*int(res["amount"]))
#             day = datetime_after.day
#             month = datetime_after.month
#
#         elif find_dict_match(res["time_range"], time_measure) == 'years':
#             year += int(res["amount"])
#
#     return json_output



    # # КАЖДОЕ ВРЕМЯ
    # if 'every' in res:
    #     if 'amount' in res and not res["amount"] == '':
    #         repeat_every = res["every"] + ' ' + res["amount"] + ' ' + res["time_range"]
    #     elif 'amount' in res and res["amount"] == '':
    #         repeat_every = res["every"] + ' ' + res["time_range"]


    # cprint(repeat_after, 'magenta')
    # cprint(repeat_every, 'cyan')

    # # ОБЩИЙ ВЫВОД
    # if status == FAILED:
    #     task = None
    #     hour = None
    #     minute = None
    #     day = None
    #     month = None
    #     year = None
    #
    # json_output = "MESSAGE=", {'STATUS': status, 'TEXT': task,
    #       'PARAMS': {'repeat_every': '', 'repeat_after': repeat_after},
    #        'DATE': {'hour': hour, 'minute': minute, 'day': day, 'month': month, 'year': year}}