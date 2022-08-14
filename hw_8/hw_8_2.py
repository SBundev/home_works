n = int(input("Введите размер матрици: "))
import random
a = [[random.randint(-100, 100)  for i in range(n)] for j in range( n)]
for b in a:
    print(b)
print("Сумма чисел по диагонали =", sum(a[i][i]for i in range(n)))
print("сумма чисел последнего столбца = ", sum(a[i][n-1] for i in range(n)))
