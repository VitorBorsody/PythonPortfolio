from math import factorial
# First form

n1 = int(input("Enter a number to calculate factorial: "))
print(f'{n1}! = {factorial(n1)}')

# Second form

n2 = int(input("Enter a number to calculate factorial: "))

c = n2
f = 1
print(f'Calculating {n2}! = ', end = '')
while c>0:
   print(f' {c} ', end = '')
   print(' x ' if c > 1 else ' = ', end = '')
   f *= c
   c -= 1
print(f'{f}', end = '')

