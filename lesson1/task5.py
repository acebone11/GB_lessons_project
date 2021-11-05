income = float(input("Введите выручку "))
cost = float(input("Введите расход "))
if income > cost:
    print("выручка больше расхода ")
    profit = income - cost
    human = int(input("введите количество сотрудников "))
    final_result = profit / human
    print("Выручка на одного сотрудника равна ", final_result)
else:
    print("компания несет убытки")
