var_string = input("Введите текст: ")
var_string = var_string.lower()
var_char = input("Введите символ: ")
count = 0
#print("Количество символов в введенной строке =", var_string.find(var_char))
for i in var_string:
    if i == var_char:
        count += 1

print("К-во введенных символ в тексте = ", count)
#    elif i != var_char:
#        print("Текст не садержит введенного символа")
