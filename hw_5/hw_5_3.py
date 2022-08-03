count_1 = 0  # К-во четных чисел
count_2 = 0  # К-во не четных чисел
count_3 = 0  # К-во введенных чисел
min = 500 ** 500
max = 0
summ = 0
mid = float(0)
i = 0
while True:
    n = int(input("""Введите любые натрульне числа,
    окончанием ввода является 0 : """))
    if n == 0:
        break
    elif n % 2 == 0:
        count_1 += 1
    elif n % 1 == 0:
        count_2 += 1
    if n > max :
        max = n
    if n < min:
        min = n
    if n != summ or n == summ:
        summ = summ + n
    if n % 2 == 0 and n % 1 == 0:
        i += 1
        count_3 = i + 1
        mid = float(summ // count_3)
print("К-во четных чисел :", count_1)
print("К-во не четных чисел :", count_2)
print("К-во введеных чисел :", count_3)
print("Максимальное введеное число : ", max)
print("Минимальное веденное число : ", min)
print("Сумма всех введеных чисел :", summ)
print("Средне арифметическое всех чисел :", mid)