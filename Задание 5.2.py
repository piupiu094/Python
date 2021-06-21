my_list = [7, 5, 3, 3, 2]
N = int(input('Введите новый элемент в виде натурального числа - '))
i = 0

for n in my_list:
    if N <= n:
        i += 1
my_list.insert(i, float(N))
print(my_list)


