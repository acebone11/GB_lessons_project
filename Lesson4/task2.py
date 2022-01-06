# Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

import random

def my_func():
    my_list = random.sample(range(2,500),30)
    list2 =[]
    for el in range(len(my_list)-1):
        if my_list[el] < my_list[el+1]:
            list2.append(my_list[el+1])
    return list2
print(my_func())
