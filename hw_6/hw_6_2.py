var_string = input("Введите текст: ")
var_char = input("Введите символ")
count = 0
for i in var_string:
    print(ord(i), end = " , ")
    if i == var_char:
        count += count
        print("К-во введенных символ в тексте = ", count)
    elif i != var_char:
        print("Текст не садержит введенного символа")
