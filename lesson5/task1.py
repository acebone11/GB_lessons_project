# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
with open("text.txt", "w") as f:
    stop = False
    while stop == False:
        vvod = input("введите текст, для завершения отправьте пустую строку")
        if vvod == "":
            stop = True
            break
        f.write(vvod)
t = open("text.txt", "r")
content = t.read()
print(content)
t.close()
