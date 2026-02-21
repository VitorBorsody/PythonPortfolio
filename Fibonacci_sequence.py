while True:
    try:
        terms = int(input('How many Fibonacci terms would you like to generate? '))

        if terms <= 0:
            print('Please enter a positive integer!')
            continue

        a = 0
        b = 1

        print("\n Fibonacci sequence: ")

        for _ in range(terms):
            print(a, end = ' ')
            a, b = b, a+b

        print()

        again = input("\n Generate another Fibonacci sequence? (y/n) ")
        if again != 'y':
            print("Program finished!")
            break

    except ValueError:
        print('Invalid input. Please enter an integer. ')
