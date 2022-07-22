import re
import random
import datetime
from termcolor import colored, cprint

string = 'к 12:01'
string_split = string.split()

def digital_time_finding(string_split, hour_k=0, minute_k=0, mask=0):
    datetime_today = datetime.datetime.today()
    mask_str_time = None
    for index_time, element_time in enumerate(string_split):
        if (':' in element_time) and (element_time.replace(':', '').isdigit()) and (len(element_time) in [4, 5]):
            word_before_element = string_split[index_time - 1]
            if len(element_time) == 4:
                hour = element_time[:-3]
                minute = element_time[2:]
            elif len(element_time) == 5:
                hour = element_time[:-3]
                minute = element_time[3:]
            if word_before_element in ['в', 'к']:
                mask_str_time = word_before_element + ' ' + element_time
            else:
                mask_str_time = element_time
        else:
            hour = datetime_today.hour
            minute = datetime_today.minute
        if hour_k == 1:
            result = hour
        elif minute_k == 1:
            result = minute
            # if len(str(minute)) == 1:
            #     result = '0' + str(minute)
            # else:
            #     result = minute
        if mask == 1:
            result = mask_str_time

    return result

print('часов: ', digital_time_finding(string_split, 1, 0))
print('минут: ', digital_time_finding(string_split, 0, 1))
print('маска: ', digital_time_finding(string_split, 0, 0, 1))


# after_time = datetime.datetime(year=int(year), month=int(mount_data), day=int(numbers))
#
# delta_time = datetime.timedelta(hours=int(hour_str), minutes=int(minutes_str))
#
# time = None
#
# if each in ['через', 'Через']:
#     time = datetime_today + delta_time
#     hour = time.hour
#     minutes = time.minute
# elif each in ['к', 'в']:
#     time = after_time + delta_time
#     hour = time.hour
#     minutes = time.minute
