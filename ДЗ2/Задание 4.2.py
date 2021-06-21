string1 = input("введите строку ")
word = []
n = 1
for elements in range(string1.count(' ') + 1):
    word = string1.split()
    if len(str(word)) <= 10:
        print(f" {n} {word [elements]}")
        n += 1
    else:
        print(f" {n} {word [elements] [0:10]}")
        n += 1
        

