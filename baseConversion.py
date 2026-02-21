print(
    'What kind of base conversion would you like?\n'
    'Enter 0 for binary\n'
    'Enter 1 for octal\n'
    'Enter 2 for hexadecimal\n'
      )

num = int(input('Enter an integer number: '))
option = int(input('Choose one of the options above: '))
if option==0:
    print('The number {} in decimal is equivalent to {} in binary'.format(num, bin(num)))
elif option==1:
    print('The number {} is equivalent to {} in octal'.format(num, oct(num)))
elif option==2:
    print('The number {} is equivalent to {} in hexadecimal'.format(num, hex(num)))
else:
    print('Enter a valid number!')