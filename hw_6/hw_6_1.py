inp_mesg = input('Введите словосочитание:')
test = len(inp_mesg.split())
var_1 = inp_mesg.find(" ")
var_2 = inp_mesg[:var_1]
var_3 = inp_mesg[var_1 + 1:]
var_2 = var_2[::-1]
var_3 = var_3[::-1]
#print(test)
#print(var_1)
#print(var_2)
#print(var_3)

if test == 2:
    print(var_2.capitalize(), var_3.capitalize())
else:
    print("Введено не два слова")