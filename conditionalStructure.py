from random import randint
from time import sleep
from datetime import date

#01

guessingGame = int(input('Enter a number:'))

print('Processing...')
sleep(2)

random_number = randint(0,5)
if 0<=guessingGame<=5:

 if guessingGame == random_number:
    print('Well done!!! You got it!')
 else:
    print(f"Unfortunately, you lost!\nThe correct number was {random_number}")

else:
    print('Enter a valid number!')

#02

speed = float(input("Enter the car's speed:"))
if speed>80:
    print(f"It's beyond the allowed limit!\nYou have to pay a fee of R$7,00 per km over the limit.\nThe fee is R${(speed-80)*7:.2f} ")
else:
    print('You are within the allowed limit!')

#03 - Even or odd?

n = int(input('Enter a number: '))
if n%2==0:
    print(f'The number {n} is even!')
else:
    print(f'The number {n} is odd!')

#04

travel_distance = float(input('Enter the travel distance: '))
if 0<=travel_distance<=200:
    print(f'You have to pay R${travel_distance*0.5:.2f}')
else:
    print(f'You have to pay R${travel_distance*0.45:.2f}')

#05 - Leap year

year = int(input('What year would you like to analyze?\nEnter zero to analyse the current year!'))
if year==0:
    year = date.today().year
if year%4 == 0 and year%100 != 0 or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f'{year} is not a leap year')

#06 - Min and max value
values = []
for i in range(1, 4):
    value = float(input(f'{i}°:'))
    values.append(value)
print(
    f'min value: {min(values)}\n'
    f'max value: {max(values)}'
)

#07 - Salary increase

worker_salary = float(input('Enter the worker salary: '))

if worker_salary>1250:
    print(f'New salary is R${worker_salary*1.1:.2f}')
else:
    print(f'New salary is R${worker_salary*1.15:.2f}')

#08 - Triangle existence theorem

a = float(input('Enter the length of the first side: '))
b = float(input('Enter the length of the second side: '))
c = float(input('Enter the length of the third side: '))

if a>0 and b>0 and c>0:
    if abs(a-b)<c<a+b:
        print('A triangle can be formed!')
        if a == b == c:
            print("It's an equilateral triangle!")
        elif a == b or a == c or b == c:
            print("It's an isosceles triangle!")
        else:
            print("It's a scalene triangle!")
    else:
        print('A triangle cannot be formed!')
else:
    print('Side lengths must be greater than 0!')

