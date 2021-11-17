import math
import os

a = -5
b = 5
h = 0.1
x = 0
temp = (a - h)
resB = 0

while temp <= (b - h):
    x = temp + h
    temp += h
    f = x * math.exp(x) + 2 * math.sin(x) - math.sqrt(abs(x ** 3 - x ** 2))
    print(f"Значение аргумента {round(temp, 2)} значение функции {round(f, 4)}")
    if abs(f % 10 > 3):
        resB += 1
print(f"количество значений из условия {resB}")

os.system("pause")
