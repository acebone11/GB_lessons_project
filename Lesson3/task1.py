try:
    def func(num1, num2):
        result = num1 / num2
        print(f"Результат деления {result}")
        return result

    my_input1 = int(input("Введите число 1 "))

    my_input2 = int(input("Введите число 2 "))


    func(my_input1, my_input2)
except ZeroDivisionError:
    print("Деление на 0 недопустимо"
          )
