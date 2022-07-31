year = int(input("Введите год от 1900 до 1_000_000: "))

if year < 2000:
    print(" введены не верные условия")
elif year > 1000000:
    print(" введены не верные условия")

elif year % 4 == 0 and year % 100 != 0:
    print("Год высокосный")
elif year % 400 == 0:
    print("Год высокосный")
else:
    print("Год не высокосный")
print("finish")
