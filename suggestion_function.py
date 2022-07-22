from termcolor import colored, cprint

string = 'тренировка каждый час в 20:19'

prefix_dictionary = {
    'в': 1,
    'через': 2,
    'кажд': 3
}
string_split = string.lower().split()   # в общий сплит добавить .lower()
print(string_split)



def get_key_by_value(value, dictionary):
    result = None
    for element in dictionary:
        if dictionary[element] == value:
            result = element
    return result


'''
функция определяющая предлоги, выделит их из общего текста и выводя индекс каждого для 
последующей обработки и занесения даты в нужную ячейку
'''

def suggestion_function(string_split, dictionary, data):
    result = None
    pre_result =None
    for element in string_split:
        for element_dict in dictionary:
            if len(element) == 6:
                element_for_comparison = element[:-2]
                if element_for_comparison in element_dict:
                    pre_result = prefix_dictionary[element_dict]
            elif len(element) == 7:
                element_for_comparison = element[:-3]
                if element_for_comparison in element_dict:
                    pre_result = prefix_dictionary[element_dict]
            elif element in element_dict:
                pre_result = prefix_dictionary[element_dict]
    if data == 1:
        result = get_key_by_value(pre_result, dictionary)
    else:
        result = pre_result

    return result

cprint(suggestion_function(string_split, prefix_dictionary, 1), 'red')