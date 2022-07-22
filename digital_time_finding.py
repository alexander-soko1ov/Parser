import datetime

string = 'в понедельник в 12:01'
string_split = string.split()

for index_time, element_time in enumerate(string_split):
    if (':' in element_time) and (element_time.replace(':', '').isdigit()) and (len(element_time) in [4, 5]):
        word_before_element = string_split[index_time - 1]
        if len(element_time) == 4:
            hour_str = element_time[:-3]
            minutes_str = element_time[2:]

        else:
            hour_str = element_time[:-3]
            minutes_str = element_time[3:]

        if word_before_element in ['в', 'к']:
            # cprint("в, к", 'yellow')
            mask_str_time = word_before_element + ' ' + element_time
        else:
            mask_str_time = element_time

    else:
        element_time = None



after_time = datetime.datetime(year=int(year), month=int(mount_data), day=int(numbers))

delta_time = datetime.timedelta(hours=int(hour_str), minutes=int(minutes_str))

time = None

if each in ['через', 'Через']:
    time = datetime_today + delta_time
    hour = time.hour
    minutes = time.minute
elif each in ['к', 'в']:
    time = after_time + delta_time
    hour = time.hour
    minutes = time.minute
