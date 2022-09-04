from random import randint


if __name__ == "__main__":
    n = int(input("Введите количество рядов матриц: "))
    m = int(input("Введите количество столбцов матриц: "))

    a = [[randint(1, 50) for i in range(n)] for j in range(m)]
    for b in a:
        k = 0
        for i in b:
            k += i
        for j in range(n):
            if b[j] < 10:
                print("   {}".format(b[j]), end=' ')
            else:
                print("  {}".format(b[j]), end=' ')
        print("  |{}".format(k), end=' ')
        print()
    for i in range(m):
        print(" ---", end='')
    print()
    for i in range(n):
        k = 0
        for j in range(m):
            k += a[j][i]
        print("   {}".format(k), end='')
    print()
