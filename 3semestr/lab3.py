import math
import os
import sys


count = int(input("Введите n"))


def sum1():
    n = 1
    sum = 0
    for n in range(count):
        a = (-1) ** n * (1 / (n ** 2 + n + 2))
        n += 1
        sum = sum + a
    print(sum, "Сумма ряда")


sum1()


