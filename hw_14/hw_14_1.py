from random import randint

if __name__ == "__main__":
    n = int(input("Введите количество рядов матриц: "))
    strim = [[randint(1, 50) for i in range(n)] for j in range(m)]