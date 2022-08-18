import random
n = dict({k: random.randint(1, 10) for k in range(1, 21)})
print(n)
k = 1
for i in list(n.values()):
    k *= i
print(k)
