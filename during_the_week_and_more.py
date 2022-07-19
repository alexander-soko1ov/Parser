import re
from termcolor import colored, cprint

string = 'на 2-3 дня'

string_split = string.split()
print(string_split)



def finding_matches(string_split, dictionary):
    for element in string_split:
        for element_dict in dictionary:
            if (element_dict[:-1] == element) or \
                    (element_dict == element) \
                    or (element_dict == element[:-1]) or \
                    (element_dict[:-1] == element[:-1]):
                result = element_dict
                data = dictionary[result]
    return data

dictionary_datetime = {
    'минута': 'minute',
    'час': 'hour',
    'день': 'day',
    'дне': 'day',
    'неделя': 'week',
    'месяц': 'month',
    'год': 'year'
}

for element in string_split:
    element_on_right = None

    if element in ['на']:
        index_element = string_split.index(element) + 1
        element_on_right = string_split[index_element]

        if ('-' in element_on_right) and (element_on_right.replace('-', '').isdigit()) and (len(element_on_right) in [3, 5]):
            for element_data in element_on_right:

                if element_data == '-':
                    index_data_l = element_on_right.index(element_data) - 1
                    index_data_r = element_on_right.index(element_data) + 1
                    if element_on_right[index_data_l].isdigit() and element_on_right[index_data_r].isdigit():

                        datetime_element_on_right = finding_matches(string_split, dictionary_datetime)
                        print(element, element_on_right[index_data_l], element_data, element_on_right[index_data_r], datetime_element_on_right)

# result = re.findall(r'[нН][аА][\s][\d][\d]?[-]?[\d]?[\d]', string)