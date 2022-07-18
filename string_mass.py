import re
from termcolor import colored, cprint

message = "/тренировка_каждый_понедельник_20:19"

if isinstance(message, str):
    message_split = re.split(' |_|/', message)



print(message_split)

