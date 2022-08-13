n = int(input("Введите размер матрици: "))

a = [ [n-i if j % 2 == 1 else i-n for i in range(-1, -n-1, -1)] for j in range(1, n**2-1, n)]

print(a)

