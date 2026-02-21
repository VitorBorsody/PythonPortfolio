print('Please, enter the following numbers below:')
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

maximum = a
minimum = a

if b>maximum:
    maximum = b

if c>maximum:
    maximum = c

if b<minimum:
    minimum = b

if c<minimum:
    minimum = c


print('The max value between {}, {} and {} is: {}'.format(a, b, c, maximum)  )

print('The min value between {}, {} and {} is: {}'.format(a, b, c, minimum))