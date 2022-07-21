import datetime
from termcolor import colored, cprint

string = 'фыв 123 фы 123 в пятницу'
string_split = string.split()

days_of_the_week = {
    'понедельник': 0,
    'вторник': 1,
    'среда': 2,
    'четверг': 3,
    'пятница': 4,
    'суббота': 5,
    'воскресенье': 6
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

def get_key_by_value(value, dictionary):
    result = None
    for element in dictionary:
        if dictionary[element] == value:
            result = element
    return result

datetime_today = datetime.datetime.today()
weekday = datetime_today.weekday()

date_difference = 0
days_week = None

for weekday_after in string_split:
    # cprint(finding_matches(string_split, days_of_the_week, 1), 'red')
    date_def = finding_matches(string_split, days_of_the_week, 1)
    if date_def in [0, 1, 2, 3, 4, 5, 6]:
        weekday_after = get_key_by_value(date_def, days_of_the_week)
        if days_of_the_week[weekday_after] < weekday:
            date_difference = days_of_the_week[weekday_after] - weekday + 7
        elif days_of_the_week[weekday_after] == weekday:
            date_difference = days_of_the_week[weekday_after] - weekday + 7
        elif days_of_the_week[weekday_after] > weekday:
            date_difference = days_of_the_week[weekday_after] - weekday

number = datetime_today + datetime.timedelta(days=date_difference, weeks=0)
year = number.year
mount = number.month
day = number.day
hour = number.hour
minutes = number.minute
print(day, mount, year)
print(hour, ":", minutes)