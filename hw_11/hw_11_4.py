def table(func):
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        k = set(g)
        k = list(k)
        k.sort()
        print(" ", "_" * len(str(k[-1])), " ", "_" * 13, "_" * 8)
        for i in range(len(k)):
            print("|", str(k[i]).ljust(len(str(k[-1])), " "), "|",
                  "кратное 3".ljust(11, " ") if k[i] % 3 == 0
                  else "не кратное 3".ljust(11, " "),
                  "|", "парное".ljust(8, " ") if k[i] % 2 == 0
                  else "не парное".ljust(8, " "), "|")
            print("|", "-" * len(str(k[-1])), "|", "-" * 12, "|", "-" * 8, "|")
    return wrapper


@table
def numbers(x):
    import random
    n = set(random.randint(1, 10000) for _ in range(x))
    return n


numbers(5)
