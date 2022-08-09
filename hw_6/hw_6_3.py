x = input("Введите число от 3 до 9 : ")
while True:
    if not x.isdigit():
        print("Введено не число")
        break
    elif   int(x)< 3 or int(x) > 9:
        print("Введено не верное число")
        break
    else:
        c = int(x)
        for i in range(1, c+1):
            for k in range(1, i+1):
                print(k, end=" ")
            for k in range(i-1, 0, -1):
                print(k, end=" ")
            print()
        break