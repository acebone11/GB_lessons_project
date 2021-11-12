


sum_res = 0
ex = True
while ex == True:
    input_data = input("Введите числа для сложения разделенные пробелом для выхода наберите 'q'>>>  ").lower().split()
    res = 0

    for el in range(len(input_data)):

        if input_data[el] == 'q':
            print('выход')
            ex = False
            break
        else:
            res = res + float(input_data[el])
    print(f"результаты текущего вычисления {res}")
    sum_res = sum_res + res
    print(f"общая сумма равна = {sum_res}")

