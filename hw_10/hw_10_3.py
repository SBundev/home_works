flat_n = {i for i in range(1, 76)}
flat_m = {i for i in range(76, 103)}
flat_n_m = {i for i in range(1, 14)}
k = flat_n | flat_m
n = k - flat_n_m
print("В доме N живет ", len(n), "семей")
