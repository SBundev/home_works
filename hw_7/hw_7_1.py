lst = list(input("Введите список состоящий из чисел : ").split())
k = int(input("Введите индекс элемента из списка : "))
for n in range(k,len(lst) - 1):
    lst[n] = lst[n+1]
lst.pop()
print(lst)
