def except_(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError as t:
        print(f"Неверный ввод, одна или обе переменных не являются числом :{t}")
        c: str = str(a) + str(b)
        print("Конкатенация переменных А и В = ", c)
    else:
        print("Все правильно. Вы ввели числа", a, "и ", b, ", их сумма = ", a+b)
    finally:
        print("Конец прграммы ")


if __name__ == "__main__":
    a = input("Введите число A: ")
    b = input("Введите число B: ")
    print(except_(a, b))
