word = input("Введите строку ")
num = 1
for el in range(word.count(' ') + 1):
    word_new = word.split()

    if len(str(word_new)) <= 10:
        print(num, word_new[el])
        num += 1
    else :
        print(num,word_new[el][0:10])
        num += 1