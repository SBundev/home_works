lst_1 = list(input("Введите список состоящий из чисел : ").split())
lst_2 = list(input("Введите список состоящий из чисел : ").split())
count = 0
for n in range(0,len(lst_1)-1):
    for k in range(0,len(lst_2)-1):
        if lst_1[n] != lst[k]:
            count += 1
        else:
            print("Нет уникальных чисел")

Print(count)
