from random import randint

def dict_handler(dct, key, default_value):
    try:
        #value = dct[key]
        keys = dct.keys()
        assert key in keys, "yt d[jlbn"
    except KeyError as k:
        print(f"данный ключ не входит в существующий словарь :{k}")
        dct_1 = dict.fromkeys(key, default_value)
        print("Словарь ", dct_1, " с ключем", key, " не входит в существующий словарь", dct)
    else:
        dct_1 = dict.fromkeys(key, default_value)
        print("Все правильно, ключ ", key, " входит в словарь", dct, ", из словаря", dct_1)

    finally:
        print("Конец прграммы ")


if __name__ == "__main__":
    n = [randint(1, 10) for i in range(0, 20)]
    r = [randint(10, 99) for c in range(0, 20)]
    dct = {k: v for k, v in zip(n, r)}
    key = str(input("Введите число key: "))
    default_value = str(input("Введите число default_value: "))
    print(dct)
    print(dict_handler(dct, key, default_value))
