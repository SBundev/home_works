dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}

dictionary = dictionary_1 | dictionary_2
print(dictionary)

c = {**dictionary_1, **dictionary_2}
print(c)

dictionary_1.update( dictionary_2)
print(dictionary_1)