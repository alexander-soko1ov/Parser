import re
import random
import datetime
from termcolor import colored, cprint

string = 'в 12:16'
string_split = string.split()
print(string_split)


def digital_time_finding(string_split, hour_k=0, minute_k=0, mask=0):
    """функция работает с датами в цифровом формате 'в 12:01, к 18:45',
     выводит часы, минуты, маску """
    datetime_today = datetime.datetime.today()
    hour = datetime_today.hour
    minute = datetime_today.minute

    mask_str_time = None
    result = None

    for index_time, element_time in enumerate(string_split):
        if (':' in element_time) and (element_time.replace(':', '').isdigit()) and (len(element_time) in [4, 5]):

            word_before_element = string_split[index_time - 1]
            if len(element_time) == 4:
                hour = element_time[:-3]
                minute = element_time[2:]
            elif len(element_time) == 5:
                hour = element_time[:-3]
                minute = element_time[3:]
            if word_before_element in ['в', 'к', 'на']:
                mask_str_time = word_before_element + ' ' + element_time
            else:
                mask_str_time = element_time


    if hour_k == 1:
        result = hour
    elif minute_k == 1:
        result = str(minute).lstrip('0')

    if mask == 1:
        result = mask_str_time

    return result

print('часов: ', digital_time_finding(string_split, 1, 0))
print('минут: ', digital_time_finding(string_split, 0, 1))
print('маска: ', digital_time_finding(string_split, 0, 0, 1))