import datetime

# работа с datetime, получение года, месяца, даты и времени, исходя из изначальных условий
time_today = datetime.datetime.today()
print('Сейчас: ', time_today)
year = time_today.year
mount = time_today.month
day = time_today.day
hour = 0
minute = 90

after_time = datetime.datetime(year=year, month=mount, day=day)

delta_time = datetime.timedelta(hours=hour, minutes=minute)

through_time = time_today + delta_time

at_the_time = after_time + delta_time


print('Через время: ', through_time)
print('В назначенное время: ', at_the_time)


# # определение месяца
# dictionary_month = {
#     'января': 'January',
#     'февраля': 'February',
#     'марта': 'March',
#     'апреля': 'April',
#     'мая': 'May',
#     'июня': 'June',
#     'июля': 'July',
#     'августа': 'August',
#     'сентября': 'September',
#     'октября': 'October',
#     'ноября': 'November',
#     'декабря': 'December'
# }

# string = "май"
# string = string.lower()
#
# dictionary_month = {
#         'января': 1,
#         'февраля': 2,
#         'март': 3,
#         'апреля': 4,
#         'мая': 5,
#         'июня': 6,
#         'июля': 7,
#         'августа': 8,
#         'сентября': 9,
#         'октября': 10,
#         'ноября': 11,
#         'декабря': 12
# }
#
# if (element[:len(element)-1] in dictionary_month ) or (element in dictionary_month ):
# #     if (element[:-1] == string) or (element == string) \
# #             or (element == string[:-1]) or (element[:-1] == string[:-1]):
# #         print("месяц: ", dictionary_month[element])


# # новый метод, на замену message.replace()
# text = 'Подписать_служебку_23_февраля 23 февраля'
#
#
# string = text.split()
# print(string)
#
# # print(type(string))
#
# index_data = string.index('23')
#
#
# string_not_data = string.pop(index_data)
#
#
# index_mount = string.index('февраля')
#
# string_not_mount = string.pop(index_mount)
#
#
# print(string)

# text = 'час'
# text_split = text.split()
#
# print(text_split)
#
# dictionary_time = {
#         'минут': 1,
#         'часа': 2,
#         'дней': 3
# }
#
# day = None
# hour = None
# minute = None
#
# for element in text_split:
#
#
#
#     for dictionary_time_element in dictionary_time:
#         print()
#
#         if (dictionary_time_element == element) or (dictionary_time_element[:-1] == element) or \
#                 (dictionary_time_element == element[:-1]) or (dictionary_time_element[:-1] == element[:-1]):
#             print(dictionary_time_element)
#             # if dictionary_time_element == 'минут':
#             #     index = text_split.index(dictionary_time_element)
#             #     minute = text_split[index - 1]
#             #     print(minute, 'минут')
#             # elif dictionary_time_element == 'часов':
#             #     index = text_split.index(dictionary_time_element)
#             #     hour = text_split[index - 1]
#             #     print(hour, 'часов')
#             # elif dictionary_time_element == 'дней':
#             #     index = text_split.index(dictionary_time_element)
#             #     day = text_split[index - 1]
#             #     print(day, 'дней')

#
# print(day, 'дней')
# print(hour, 'часов')
# print(minute, 'минут')
