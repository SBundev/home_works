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