sub = {}
with open('test_6.txt', 'r') as init_f:
    for line in init_f:
        subject, lecture, practice, l = line.split()
        sub[subject] = int(lecture) + int(practice) + int(l)
    print(f'Общее количество часов по предмету - \n {sub}')
