import datetime

string = 'в среду'
string_split = string.split()
print(string_split)

days_of_week_dict = {
    'понедельник': 0,
    'вторник': 1,
    'среда': 2,
    'четверг': 3,
    'пятница': 4,
    'суббота': 5,
    'воскресенье': 6
}

def get_key_by_value(value, dictionary):
    """возвращет ключ по значению из словаря"""
    result_key = None
    for element in dictionary:
        if dictionary[element] == value:
            result_key = element
    return result_key

def finding_matches(string_split, dictionary, text=0):
    """определяет дни недели, месяцы и другое, отбрасывая окончания,
    возвращает:
        0 - тектовый элемент словаря
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


def day_of_week(string_split, format_data=0):
    """определяет дни недели, возвращает:
    дату в формате листа [день, месяц, год, час, минута]"""

    datetime_today = datetime.datetime.today()
    weekday_today = datetime_today.weekday()
    day_every = 0

    for day_of_week in string_split:
        date_def = finding_matches(string_split, days_of_week_dict, 1)
        if date_def in [0, 1, 2, 3, 4, 5, 6]:
            day_of_week = get_key_by_value(date_def, days_of_week_dict)
            if days_of_week_dict[day_of_week] < weekday_today:
                day_every = days_of_week_dict[day_of_week] - weekday_today + 7
            elif days_of_week_dict[day_of_week] == weekday_today:
                day_every = days_of_week_dict[day_of_week] - weekday_today + 7
            elif days_of_week_dict[day_of_week] > weekday_today:
                day_every = days_of_week_dict[day_of_week] - weekday_today
        # else:
        #     day_of_week = get_key_by_value(weekday_today, days_of_week_dict)
    number = datetime_today + datetime.timedelta(days=day_every)
    day = number.day
    mount = number.month
    year = number.year
    hour = number.hour
    minute_pre_res = number.minute
    if len(str(minute_pre_res)) == 1:
        minute = '0' + str(minute_pre_res)
    else:
        minute = minute_pre_res
    pre_result = [day, mount, year, hour, minute]
    if format_data == 0:
        result = number
    elif format_data == 1:
        result = pre_result

    return result

# print(day_of_week(string_split).minute)

print(day_of_week(string_split,1))