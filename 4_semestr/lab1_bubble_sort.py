
import timeit
code_test = """
from random import randint
N = 10
a =[]
for i in range(N):
    a.append(randint(1,99))
def bubble_sort(array):
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff
print(f'несортированный массив {a}')
bubble_sort(a)
print(f'Сортированный массив {a}')
"""
elapsed_time = timeit.timeit(code_test, number=10)
print(elapsed_time)

