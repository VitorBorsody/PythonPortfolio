k1 = ('Car', 'Store', 'Pencil', 'Notebook', 'Set of chairs', 'Bootle of water')
vowels = ['a', 'e', 'i', 'o', 'u']
for item in k1:
    found = []
    for letter in item:
        if letter in vowels:
            found.append(letter)

    print(f'{item} -> {len(item)} -> ({found}) ')
 

