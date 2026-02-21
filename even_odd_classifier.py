temp = [[], []]
while True:
    try:
        n = float(input('Enter a number: '))
    except ValueError:
        print('That is not a number! ')
        continue

    if n % 2 == 0:
        temp[0].append(n)

    else:
        temp[1].append(n)


    control_variable = str(input('Do you wish to continue? (y/n) ')).strip().lower()

    if not control_variable:
        print('Input cannot be empty!')
        continue
    control_variable = control_variable[0]
    if control_variable not in ('y', 'n'):
        print('Enter a valid option! ')
        continue
    if control_variable == 'n':
        break
print('-'*30)
print(f'Even numbers: {temp[0]}')
print(f'Odd numbers: {temp[1]}')
print('-'*30)
