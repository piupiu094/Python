def sum_1 ():
    res = 0
    i = False
    while i == False:
        number = input('Введите числа через пробел или S ').split()

        res_w = 0
        for ll in range(len(number)):
            if number[ll] == 'S' or number[ll] == 's':
                i = True
                break
            else:
                res_w = res_w + int(number[ll])
        res = res_w + res
        print(f'Текущая сумма {res}')
    print(f'Финальная сумма {res}')


sum_1()
