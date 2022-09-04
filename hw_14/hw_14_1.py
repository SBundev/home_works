from random import randint
from sorti import p


if __name__ == "__main__":
    n = int(input("Введите длину списка: "))
    strim = [randint(1, 50) for i in range(n)]
    sorti_insertion(strim)
    print(strim)