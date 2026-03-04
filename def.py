from time import sleep
from math import fabs
from random import randint

#01

def customized_message(msg: str) -> None:
    size = len(msg) + 4
    print('-'*size)
    print(f'  {msg}')
    print('-'*size)


customized_message('Hello! ')

#02

def sum_numbers(num1: int, num2:int)->None:
    num = num1 + num2
    print(num)

print(sum_numbers(1,5))

#03

def double_the_list_values(l:list):
    i = 0
    while i<len(l):
        l[i] = 2*l[i]
        i+=1

l = [0, 1, 2, 4]
double_the_list_values(l)
print('Before: l = [0, 1, 2, 4]')
print(f'After: {l}')

#04

def calculate_area(width: float, length: float) -> float:
    customized_message('Terrain Area')
    print(f'The area of a {width}x{length} terrain is {width*length} m²')


print(calculate_area(4,5))

def customized_count(beginning, ending, step):

  if beginning < ending:
      count = beginning
      while count <= ending:
          print(f'{count}', end = ' ')
          sleep(0.5)
          count += step
      print()

  else:
      step = fabs(step)
      count = beginning
      while count>=ending:
          print(f'{count}', end = ' ')
          sleep(0.5)
          count -= step
      print()

#05

def biggest_value(*n:float)->float:

    if not n:
        raise ValueError("At least one number must be provided!")
    the_biggest = None
    for item in n:
        if the_biggest is None or item > the_biggest:
            the_biggest = item
    return the_biggest

#06

def drawn_numbers(l:list):
    for count in range(0, 5):
        l.append(randint(0, 100))
    return l

def even_numbers(l:list):
    even = list()
    for k in l:
        if k % 2 == 0:
            even.append(k)
    return sum(even)
