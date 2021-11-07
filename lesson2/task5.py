my_list = [1, 3, 3, 5, 6, 7, 8, 9, 0]
my_input = int(input("Введите элемент рейтинга"))
my_list.append(my_input)
for el in range (len(my_list)):
    my_list.sort()
    my_list.reverse()
print(f"{'Пользователь ввел число'} {my_input} {'текущий рейтинг'} {my_list}")