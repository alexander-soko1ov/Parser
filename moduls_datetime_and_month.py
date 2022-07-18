# import datetime
#
# # работа с datetime, получение года, месяца, даты и времени, исходя из изначальных условий
# time_today = datetime.datetime.today()
# # print(time_today)
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

# определение месяца

string = "МаЯ"
string = string.lower()

dictionary_month = {
        'января': 1,
        'февраля': 2,
        'марта': 3,
        'апреля': 4,
        'мая': 5,
        'июня': 6,
        'июля': 7,
        'августа': 8,
        'сентября': 9,
        'октября': 10,
        'ноября': 11,
        'декабря': 12
}

for element in dictionary_month:
    # if (element[:len(element)-1] in dictionary_month ) or (element in dictionary_month ):
    if (element[:-1] == string) or (element == string) or (element == string[:-1]) or (element[:-1] == string[:-1]):
        print("месяц: ", dictionary_month[element])
