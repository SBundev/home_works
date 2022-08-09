while True:
    inp_mesg = input('Введите словосочетание из двух слов:')
    inp_mesg = inp_mesg.lstrip()
    test = len(inp_mesg.split(" "))
    var_1 = inp_mesg.find(" ")
    var_2 = inp_mesg[:var_1]
    var_3 = inp_mesg[var_1 + 1:]
    var_2 = var_2[::-1]
    var_3 = var_3[::-1]

    if test == 2:
        print(var_2.capitalize(), var_3.capitalize())
        break
    elif test != 2:
        print("Введено словосочетание более  чем из двух слов, или из одного")