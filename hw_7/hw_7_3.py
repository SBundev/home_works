lst_1 = list(input("Введите список состоящий из чисел : ").split())
lst_2 = list(input("Введите список состоящий из чисел : ").split())
lst_3 = []
for n in lst_1:
    if n not in lst_2:
        lst_3.append(n)
for n in lst_2:
    if n not in lst_1:
        lst_3.append(n)
#print(lst_3)
print(len(lst_3))
