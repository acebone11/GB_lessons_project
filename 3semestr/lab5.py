try:
    count = int(input("Введите количество значний для ввода в массив >>> "))
except ValueError:
    print("Введен некоректный символ")

my_list = []
my_list2 = []
q = 0
for i in range(count):
    number = int(input("Введите значения массива  >>>  "))
    if str(q) not in str(number):
        my_list.append(number)
for el in my_list:
    s = str(el)
    first_digit = int(s[0])
    last_digit = int(s[-1])
    if first_digit == last_digit:
        my_list2.append(s)

    my_list2.sort()
    my_list2.reverse()

print(f"числа удовлетворяющие условию Q {my_list}")
print(my_list2)
