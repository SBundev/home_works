lst = list(input("Введите список состоящий из чисел : "))
k = int(input("Введите индекс элемента из списка : "))
lst[::] = lst[:k-1] + lst[k:] + lst[k-1:k]
lst.pop()
print(lst)
