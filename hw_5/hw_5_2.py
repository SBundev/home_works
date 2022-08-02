lim = int(input("Введите любое натуральное число: "))
lim = lim + 1

for n in range(1, lim):
    m = n
    count = 0
    while m > 0:
        m //= 10
        count += 1
#    print(count)
    x = 10 ** count
    k = n ** 2
    i = k % x
    if n == i:
        print(n)

#