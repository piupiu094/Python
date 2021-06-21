
def funstep(x, y):
    return 1 if y == 0 else funstep(x, y + 1) * 1 / x

print(funstep(100, -3))
