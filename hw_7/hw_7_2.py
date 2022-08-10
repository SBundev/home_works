lst = list(input("Введите список состоящий из чисел : ").split())
k = int(input("Введите индекс элемента из списка : "))
C = int(input("Введите число которое хотите добавить в список: "))
lst.append(0)
for n in range(len(lst)-1, k, -1):
    lst[n] = lst[n-1]
lst[k] = C
print(lst)
