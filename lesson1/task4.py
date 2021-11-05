number = int(input("Введите натуральное положительное число  "))
if number < 0:
    print("число не положительное ")
else:
    m = 0
    i = 0
    for i in range(number):

        if (number % 10 > m):
            m = number % 10
        number //= 10
print(m)
import os

os.system("pause")
