def read_int():

        try:
            i = int(input('Enter a number: '))
            return i
        except ValueError:
            print('\033[0;31mInvalid input!\033[m')
            return None


k = read_int()
