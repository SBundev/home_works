x = int(input("Введите число от 3 до 9 : "))
s = int(123456789)

while True:
    if x < 3 or x > 9:
        print("Введено не верное число")
        break
    for i in range(10):
        if i == 2:
            print("121")
