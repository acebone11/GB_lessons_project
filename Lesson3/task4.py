try:


    def my_func(x, y):
        if x > 0 or y < 0:
            result = x ** y


        return result


    x = float(input("Действительное положительное число "))
    y = int(input("Целое отрицательное число"))
    print(my_func(x, y))
except: UnboundLocalError
print("Введены неверные параметры")
