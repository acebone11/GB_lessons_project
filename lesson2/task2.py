my_list = input("Введите элементы списка через пробел ").split()
print(my_list)
for i in range(0, len(my_list) - 1, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)
