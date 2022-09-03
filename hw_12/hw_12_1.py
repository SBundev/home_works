import random


def sort_a_s():
    for i in range(n):
        for j in range(n):
            if a[i][j] <= 9:
                print('    {}'.format(a[i][j]), end=' ')
            else:
                print('   {}'.format(a[i][j]), end=' ')
        print()
    for k in range(n):
        if s[k] < 100:
            print('  ', s[k], end=' ')
        else:
            print(' ', s[k], end=' ')


def sort():
    for i in range(n):
        for j in range(n - i - 1):
            if s[j + 1] < s[j]:
                s[j], s[j + 1] = s[j + 1], s[j]
                for stlb in range(n):
                    a[stlb][j], a[stlb][j + 1] = a[stlb][j + 1], a[stlb][j]

    for stlb in range(n):
        if stlb % 2 == 0:
            for i in range(n):
                for j in range(n - 2, i - 1, -1):
                    if a[j + 1][stlb] > a[j][stlb]:
                        a[j][stlb], a[j + 1][stlb] = a[j + 1][stlb], a[j][stlb]
        else:
            for i in range(n):
                for j in range(n - 2, i - 1, -1):
                    if a[j + 1][stlb] < a[j][stlb]:
                        a[j][stlb], a[j + 1][stlb] = a[j + 1][stlb], a[j][stlb]


n = int(input("Введите размер матрици, не меньше 5-ти: "))
if n < 5:
    print("Вы вввели не верное число")
else:
    a = [[random.randint(1, 50) for i in range(n)] for j in range(n)]
    s = (list(map(sum, zip(*a))))
    print("Матрица до сортировки")
    sort_a_s()
    print()
    print("Матрица после сортировки")
    print()
    sort()
    sort_a_s()
