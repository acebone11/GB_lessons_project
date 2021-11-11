# . Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
a = int(input('a'))
b = int(input('b'))
c = int(input('c'))


def my_func(a, b, c):
    if a > b and a > c:
        max1 = a
    if  b > c:
        max2 = b
    else:
        max2 = c
    max3 = max2 + max1
    print(max3)


my_func(a,b,c)
