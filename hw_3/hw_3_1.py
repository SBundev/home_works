integer1 = input("Привет, меня зовут Сергей. Как тебя зовут?  ")
var1 = str(integer1)
print("Привет " + var1 + "!")
integer2 = input("Загадай целое число " + var1 + ": ")
var2 = int(integer2)
integer3 = input("Загадай другое целое число, " + var1 + ": ")
var3 = int(integer3)
print("Сумма чисел "+ var1 + ", ровна: ", end="")
print(var2 + var3)