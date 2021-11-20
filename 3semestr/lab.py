
# с заданным диапозоном
my_list = []
a = 1
b = 31
k =0
c =0
for h in range(a,b):
    my_list.append(h)
print(my_list)

for i in range(len(my_list)):
    if  my_list[i] in my_list[0:i]:
        k+=1
print(k)
# с указанным вручную диапозоном
#
my_array =[1,2,2,3,4,4]
for i in range(len(my_array)):
    if my_array[i] in my_array[0:i]:
        c+=1
print(c)
