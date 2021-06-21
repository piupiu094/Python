kol = int(input("Введите количество элементов списка "))
my_list = []
i = 0
elements  = 0
while i < kol:
    my_list.append(input("Введите следующее значение списка "))
    i += 1

for el in range(int(len(my_list)/2)):
        my_list[elements ], my_list[elements  + 1] = my_list [elements  + 1], my_list[elements ]
        elements  += 2
print(my_list) 
