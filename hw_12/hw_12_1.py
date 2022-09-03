import random


def sort():
    summ = len(s)
    for i in range(summ):
        for j in range(summ - 2, i - 1, -1):
            if s[j + 1] < s[j]:
                s[j], s[j + 1] = s[j + 1], s[j]
    return summ

    k = len(a)
    for i in range(k):
        for j in range(k - 2, i - 1, -1):
            if a[j + 1] < a[j]:
                a[j], a[j + 1] = a[j + 1], a[j]




n = int(input("Введите размер матрици, не меньше 5-ти: "))
if n < 5:
    print("Вы вввели не верное число")
else:
    a = [[random.randint(1, 50) for i in range(n)] for j in range(n)]
    #sort()
    print(*a, sep='\n')
    s = (list(map(sum, zip(*a))))
    sort()
    print(*s)
