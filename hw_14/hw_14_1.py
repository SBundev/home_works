from random import randint
from sorti import sorti_quick


if __name__ == "__main__":
    n = int(input("Введите длину списка: "))
    strim = [[randint(1, 50) for i in range(n)]]
    sorti_quick(strim)
    print(strim)