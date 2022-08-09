var_string = input("Введите текст: ")
var_string = var_string.lower()
var_char = input("Введите символ: ")
count_1 = 0
 #  Вариант №1
for i in var_string:
    if i == var_char:
        count_1 += 1
print("К-во введенных символов в строке = ", count_1)

 #  Вариант №2

var = -1
count_2 = 0
while True:
    var = var_string.find(var_char, var + 1)
    if var == -1:
        break
    count_2 += 1
print("К-во введенных символов  в строке =", count_2)
