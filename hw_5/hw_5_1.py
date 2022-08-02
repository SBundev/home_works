a = int(input("Введите натуральное число: "))
result = "No"
while a > 0:
    b = a // 10
    c = a % 10
    a //= 10
    while b != 0:
        if c == b % 10:
            result = "Yes"
        b //= 10
print(result)