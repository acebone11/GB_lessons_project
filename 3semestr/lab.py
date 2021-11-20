
# с заданным диапозоном
my_list = []
a = 1
b = 31
k =0
c =0
m = int(input("число М  "))
for h in range(a,b):
    my_list.append(h)
print(my_list)

for i in range(len(my_list)):
    if my_list[i] <= m and not my_list[i] in my_list[0:i]:
        k+=1
print("число различных элементов до M  ",  k)
