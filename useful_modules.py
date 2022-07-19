
# определение месяца, используя словарь с ключами в виде строки
string = '17 мая'

dict_day_of_week = {
    'Май мая май Мая': 5
}
year = 0
month = 0
day = 0
hour = 0
minute = 0

split_string = list(string.split())

for day_of_week in dict_day_of_week:
    list_day_of_week = list(day_of_week.split())
    if split_string[1] in list_day_of_week:
        month_index = dict_day_of_week[day_of_week]
        month = int(dict_day_of_week[day_of_week])
print(month)


# определение времени работы программы
import time
start_time = time.time()
print(time.time() - start_time)
