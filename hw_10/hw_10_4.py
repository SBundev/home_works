clas = {i for i in range(1, 53)}
icon = {i for i in range(1, 24)}
mark_icon = {i for i in range(1, 17)}
x = icon - mark_icon
mark = {i for i in range(len(x), len(x) + 36)}
y = icon | mark
z = clas - y
print("В классе ", len(z), "учеников не увлекаются коллекционированием")
