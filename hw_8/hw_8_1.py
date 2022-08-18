n = int(input("Введите размер матрици: "))
a = [[i if j % 2 == 1 else j for i in range(-n, 0)] for j in range(n)]
for b in a:
    print(b)
