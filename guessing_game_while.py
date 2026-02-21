from time import sleep
count = 0
print(
    'Choose a number in the interval [0, 10]'
)
user_choice = int(input('Please enter your choice: '))
from random import randint

if 0<=user_choice<=10:
 computer_choice = randint(0,10)

 while computer_choice != user_choice:

      computer_choice = randint(0, 10)

      count += 1
      print('Processing...')
      sleep(1)
      if count == 1:
          k = "once"
      elif count == 2:
          k = "twice"
      else:
          k = f"{count} times"

      print(
          f'Computer choice: {computer_choice}\n'
          f'User choice: {user_choice}\n'
          f'The computer tried {k} '

      )



 print('Match found!')

else:
    print('Enter a valid choice, please try again!')


