def func(x=1, y=100):
    for n in range(x, y):
        for i in range(2, y+1):
            if n % i == 0 or n == i:
                break
            else:
                yield n
for i in func(10, 19):
    print(i, end=" ")
