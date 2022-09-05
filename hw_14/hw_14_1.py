from random import randint
from sorti import *


if __name__ == "__main__":
    n = int(input("Введите длину списка: "))
    strim_1 = [randint(1, 50) for i in range(n)]
    strim_2 = [randint(1, 50) for i in range(n)]
    strim_3 = [randint(1, 50) for i in range(n)]
    sorti_bubble(strim_1)
    print(strim_1)
    sorti_insert(strim_2)
    print(strim_2)
    sorti_quick(strim_3)
    print(strim_3)