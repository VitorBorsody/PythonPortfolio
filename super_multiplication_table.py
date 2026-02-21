while True:
    n = int(input('What number would you like to analyse the multiplication table for? '))
    if n < 0:
        break
    for i in range(1,11):

        print(f'{n}x{i} = {n*i}')

print('The multiplication table program has been completed!')