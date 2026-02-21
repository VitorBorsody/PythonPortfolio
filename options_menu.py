n1 = float(input('Enter the first number: '))
n2 = float(input('Enter the second number: '))

while True:

    print(
        'Welcome to the options menu!\n'
        'Choose an option below:\n'
        
        '[1] - Sum\n'
        '[2] - Multiply\n'
        '[3] - The largest\n'
        '[4] - Enter new numbers\n'
        '[5] - Quit'
    )
    option = int(input('Choose an option above: '))

    if option == 1:
        n = n1 + n2
        print(n)
    elif option == 2:
        n = n1*n2
        print(n)
    elif option == 3:
        print(max(n1, n2))
    elif option == 4:
        n1 = float(input('Enter the first number: '))
        n2 = float(input('Enter the second number: '))
    elif option == 5:
        break
    else:
        print('Enter a valid option')

