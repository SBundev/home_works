import random
n = [random.randint(1, 50) for i in range(0, 10)]
r = [random.randint(50, 99) for c in range(0, 10)]
print(type(n))
dct = {k: v for k, v in zip(n, r)}
print(dct)
