a = int(input("Введите натуральное число: "))
for i in range(a):
    b = i ** 2
    if b > a:
        break
    elif b <= a:
        print("Квадрат числа : ", i, "=", b)