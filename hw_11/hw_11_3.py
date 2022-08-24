def func(x=1, y=100):
    prosto_namber = []
    for n in range(x, y):
        for i in range(1, 100):
            if n % i == 0:
                break
            else:
                prosto_namber.append(n)
    return prosto_namber

print(func(10, 19))
