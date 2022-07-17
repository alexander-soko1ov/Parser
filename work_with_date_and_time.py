# from datetime import datetime
#
#
# time = datetime.now().time()
#
# print('часов:', time.strftime("%H"))
# print('минут:', time.strftime("%M"))
#
# date = datetime.now()
# print(date.strftime("%A, %d %B, %Y"))

t1 = "13:00"

t2 = t1.split(":")

print('Часов: ', t2[0])
print('Минут: ', t2[1])