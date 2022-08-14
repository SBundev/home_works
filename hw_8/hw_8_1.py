n = int(input("Введите размер матрици: "))

#a = [[i if j % 2 == 1 else i == j for i in range(-n, 0, 1)] for j in range(0, n**2, n)]

a = [[i if j % 2 == 1 else j%2**j  for i in range(-n,0)] for j in range( n)]

for row in a:
    print(' '.join([str(elem) for elem in row]))

#"if j % 2 == 1 else n-i"4