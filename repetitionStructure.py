from time import sleep

# Countdown

for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('\033[1;32mHappy new year!\033[m')

#Even numbers up to 50

for i in range(0, 52, 2):
    if i%2==0:
        print(i)

#Display odd numbers that are multiples of three
Sum = 0
count = 0
for i in range(1, 500):
    if i%2!=0 and i%3==0:
        Sum += i
        count += 1

print(
    'The sum of the {} requested numbers is: {}'.format(count, Sum)
)

# Read integer numbers and display only the sum of the even numbers

Sum = 0
for i in range(1, 7):
  n1 = int(input('Enter an integer number: '))
  if n1%2==0:
      Sum += n1
print('The sum of the even numbers is: {}'.format(Sum))

# Arithmetic progression

a1 = float(input('Enter the first term: '))
common_difference = float(input('Enter the common difference: '))
for i in range(1, 11):
    term_position = a1 + (i-1)*common_difference
    print(term_position)

# Prime numbers - A prime number is divisible only by 1 and itself

k = int(input('Enter the integer number: '))
divisor = 0
for i in range(1, k + 1):
    if k%i==0:
        divisor += 1
        print(f'\033[31m{i}\033[m', end=' ')
    else:
        print(f'{i} ', end=' ')
print()
if divisor == 2:
    print(
        f'{k} is a prime number, because it has exactly two divisors')
else:
    print(f"{k} is not a prime number, because it has {divisor} divisors")





