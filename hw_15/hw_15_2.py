from random import randint


def dict_handler(dct, key, default_value):
    try:
        key_1 = int(key)
        value = dct[key_1]
    except ValueError as t:
        print(f"Неверный ввод, введенная переменная  не являются числом :{t}")
    except KeyError as k:
        print(f"Есть исключение, данный ключ {k},"
              f"не входит в существующий словарь ")
        dct_1 = dict.fromkeys(key, default_value)
        print("Словарь ", dct_1, " с ключем", key,
              ", не входит в существующий словарь", dct)
    else:
        dct[key] = default_value
        print(f"Все правильно, ключ ", key, f" входит в словарь,"
                                            f" со значение {default_value}")

    finally:
        print("Конец прграммы ")


if __name__ == "__main__":
    n = [randint(1, 10) for i in range(0, 10)]
    r = [randint(10, 99) for c in range(0, 10)]
    dct = {k: v for k, v in zip(n, r)}
    key = input("Введите число key, от 1 до 10 : ")
    default_value = input("Введите число default_value: ")
    dict_handler(dct, key, default_value)
