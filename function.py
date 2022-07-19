string = 'фывыфв  фывф вторник'
string_split = string.split()
print(string_split)

days_of_the_week = {
    'понедельник': 1,
    'вторник': 2,
    'среда': 3,
    'четверг': 4,
    'пятница': 5,
    'суббота': 6,
    'воскресенье': 7
}

dictionary_month = {
        'января': 1,
        'февраля': 2,
        'март': 3,
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

def finding_matches(string_split, dictionary):
    for element in string_split:
        for element_dict in dictionary:
            if (element_dict[:-1] == element) or \
                    (element_dict == element) \
                    or (element_dict == element[:-1]) or \
                    (element_dict[:-1] == element[:-1]):
                result = element_dict
    return result

print(finding_matches(string_split, days_of_the_week))
