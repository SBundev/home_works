n = "pythonist"
lst = list(n)
dict_1 = dict.fromkeys(lst)
for i in lst:
    dict_1[i] = lst.count(i)
print(dict_1)
