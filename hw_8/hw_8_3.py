import random
a = [random.randint(-100, 100) for i in range(15)]
b = sum(i if i % 2 == 0 else 0 for i in a)
c = sum(i if i % 2 != 0 else 0 for i in a)
if b > c:
    print("да")
else:
    print("Нет")
# print(a,b,c)
