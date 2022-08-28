def func(x, y):
    summ = False
    for i in range(1, x + 1):
        for n in range(1, x + 1):
            if i + n == y:
                summ = True
                break
    return summ


print(func(10, 19))
print(func(8, 22))
