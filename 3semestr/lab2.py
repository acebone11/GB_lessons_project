import math
import os





def func_lab4():
    check = True
    last_num = 0
    counter = 0

    try:
        while check == True:
            num = int(input("Введите целое число, для выхода введите 0 >>>  "))

            if num == 0:
                check = False
                break
            digit = 3
            if str(digit) in str(num):
                if last_num < num:
                    last_num = num
                    counter += 1


            print(f"Маскимальное число в последовательности {last_num}")
            print("номер в последовательности  ", counter)

    except ValueError:
        print("ошибка ввода")

func_lab4()
os.system('pause')