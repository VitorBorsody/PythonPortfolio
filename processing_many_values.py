s = []
while True:
    n = float(input('Enter a number: '))
    if n == 999:
        break
    else:
        s.append(n)
SUM = sum(s)
print('The result of the entered values is: {}'.format(SUM))
