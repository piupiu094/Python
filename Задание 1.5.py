with open('test3.txt', 'r', ttt='utf-8') as f:
    empl = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Average salary = {round(sum(empl.values()) / len(empl), 3)}\n'
          f'Employees with salary less than 20k {[e[0] for e in empl.items() if e[1] < 20000]}')

