# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv

script_name, work_hour, hour_price, bonus = argv
print('название скрипта', script_name)
print('количество часов', work_hour)
print('цена часа', hour_price)
print('премия', bonus)
print('зарплата', (float(work_hour) * float(work_hour))*float(bonus))
