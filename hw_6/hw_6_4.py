str = input("Введите не меньше 15-ти любых символов : ")

print("третий символ вашего ряда = ", str[2])
print("Предпоследний  символ вашего ряда = ", str[-2])
print("Первых пять символов вашего ряда = ", str[0:5])
print("Ваш ряд без последних двух символов = ", str[0:-2])
print("Все парные символы вашего ряда  = ", str[1::2])
print("Все непарные символы вашего ряда  = ", str[2::2])
print("Все  символы вашего ряда в обратном порядке  = ", str[-1::-1])
print("Все  символы вашего ряда в обратном порядке через единицу  = ", str[-1::-2])
print(len(str))