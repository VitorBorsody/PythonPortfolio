print('-'*30)
print(f'{str('Price list'):^30}')
print('-'*30)
items_list = (
    'Fridge', 1900,
    'Notebook', 4000,
    'Laptop', 5000,
    'Set of chairs', 2500,
    'Backpack', 760
)

for pos in range(len(items_list)):

    if pos % 2 == 0:

       print(f'{items_list[pos]:.<20}', end = '')
    else:
        print(f'R${items_list[pos]:>3.2f}')
