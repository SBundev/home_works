n = """Любіть Україну, як сонце любіть,
як вітер, і трави, і води...
В годину щасливу і в радості мить,
любіть у годину негоди.

Любіть Україну у сні й наяву,
вишневу свою Україну,
красу її, вічно живу і нову,
і мову її солов'їну.

Без неї — ніщо ми, як порох і дим,
розвіяний в полі вітрами...
Любіть Україну всім серцем своїм
і всіми своїми ділами."""

b = ".", ",", "...", "-", ""
for i in range(len(b)):
    n = n.replace(b[i], "")
lst = list(n.split())
lst_1 = dict.fromkeys(n.split(), 0)

for i in lst:
    lst_1[i] = lst.count(i)

max_value = max(lst_1.values())
print(max_value)
max_key = {k: v for k, v in lst_1.items() if v == max_value}
print(max_key)

min_value = min(lst_1.values())
print(min_value)
min_key = {k: v for k, v in lst_1.items() if v == min_value}
# print(min_key)  ## выводит все ключи с минимальным значением
