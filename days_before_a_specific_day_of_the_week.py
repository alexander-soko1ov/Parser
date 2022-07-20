import datetime
from termcolor import colored, cprint

weekday_after = 'четверг'

days_of_the_week = {
    'понедельник': 0,
    'вторник': 1,
    'среда': 2,
    'четверг': 3,
    'пятница': 4,
    'суббота': 5,
    'воскресенье': 6
}

time_today = datetime.datetime.today()
date = time_today.date()
print(date)
date_delta = datetime.timedelta()
# print('Время сейчас:', time_today)


year = time_today.year
mount = time_today.month
weekday = time_today.weekday()   # сегодняшний день недели
day = time_today.day


date_difference = None

if weekday_after in days_of_the_week:
    # print(weekday_after)
    day_weekday = days_of_the_week[weekday_after]

    if days_of_the_week[weekday_after] < weekday:
        date_difference = days_of_the_week[weekday_after] - weekday + 7


    elif days_of_the_week[weekday_after] == weekday:
        date_difference = days_of_the_week[weekday_after] - weekday + 7

        # нужно прибавить одну неделю, так как уведомления на сегоднящнюю дату с её указанием никто ставить не должен


    elif days_of_the_week[weekday_after] > weekday:
        date_difference = days_of_the_week[weekday_after] - weekday


print('День недели из сообщения: ', day_weekday)  # дата из сообщения
print('День недели сейчас:', weekday)
print('разница дней недели (прибавить к дате)', date_difference)
# print('количество недель до даты: ', mount)
print('число', day + date_difference)

# today = datetime.date.today()
# result = today + datetime.timedelta(days=-today.weekday(), weeks=1)
# cprint(result, 'red')