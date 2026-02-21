temp = []
while True:
    try:
        n = float(input(f'Enter a number: '))
    except ValueError:
        print('Please, enter a number! ')
        continue
    temp.append(n)


    control_variable = str(input('Do you wish to continue [y/n]? ')).strip().lower()
    if not control_variable:
        print('Input cannot be empty! ')
        continue
    if control_variable not in ('y', 'n'):
        print('Enter either "y" or "n"! ')
        continue
    if control_variable == 'n':
        break
print('-'*50)
print(f'How many numbers were entered? {len(temp)}')
print(f'List in descending order: {sorted(temp, reverse=True)}')
if 5 in temp:
    result = True
else:
    result = False

print(f'Is 5 in the list? {result}')
print('-' * 50)
