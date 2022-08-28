def prost(x, y):
    for n in range(x, y + 1):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    break
            else:
                yield n


for k in prost(2, 100):
    print(k, end=" ")
