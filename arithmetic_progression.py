a1 = float(input('Enter the first term: '))
d1 = float(input('Enter the common difference: '))
n = 10
while n>0:

    an = a1 + (n - 1) * d1
    n -= 1
    print(f'{an: .1f}', end = '')
    print(' - ' if n>0 else '', end = '')