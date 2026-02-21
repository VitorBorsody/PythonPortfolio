even_numbers = []
odd_numbers = []
data = []

while True:
    try:
        n = int(input('Enter a number: '))
    except ValueError:
        print('That is not an integer! ')
        continue
    data.append(n)
    if n % 2 == 0:
        even_numbers.append(n)
    else:
        odd_numbers.append(n)
    control_variable = str(input('Would you like to continue [y/n]? ')).strip().lower()
    if not control_variable:
        print('Input cannot be empty! ')
        continue
    if control_variable not in ('y', 'n'):
        print('Enter a valid option! ')
        continue
    if control_variable == 'n':
        break
print('-'*50)
print(f'Complete list: {data}')
print(f'Even numbers: {even_numbers}')
print(f'Odd numbers: {odd_numbers}')
print('-'*50)
