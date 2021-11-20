def rec_func():


    sum = 0
    myarr = []
    num = input("Введите значения через пробел >>>  ").split()
    for el in num:
        myarr.append(el)
    print(myarr)
    for el in myarr:
        el = int(el)
        if int(el) % 2 != 0:
            sum = sum + el

    print(f"Сумма нечетных чисел равна {sum}")

rec_func()