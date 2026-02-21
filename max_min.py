values = []
while True:

    k = int(input('Enter a number: '))
    values.append(k)

    while True:

     control_variable = str(input('Do you want to continue? (y/n) ')).lower().strip()

     if control_variable in ('y', 'n'):
         break
     else:

         print('Please enter a valid number!')
            
    if control_variable == 'n':
        break

print(f'Maximum value: {max(values)}')
print(f'Minimum value: {min(values)}')
if len(values) > 0:
    print(f'Average group: {sum(values) / len(values):.2f}')
else:
    print('Please, enter a valid number!')
