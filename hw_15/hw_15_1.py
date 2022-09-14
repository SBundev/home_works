def except_(a, b):

    try:
        e = int(a)
        f = int(b)
    except ValueError as t:
        print(f"Неверный ввод, одна или обе переменных не являются числом :{t}")
        c: str = str(a) + str(b)
        print("Конкатенация переменных А и В = ", c)
    else:
        print("Все правильно. Вы ввели числа", e, "и ", f, ", их сумма = ", e+f)
    finally:
        print("Конец прграммы ")


if __name__ == "__main__":
    a = input("Введите число A: ")
    b = input("Введите число B: ")
    except_(a, b)
