from random import randint
items = ('Rock', 'Paper', 'Scissors')
computer_choice = items[randint(0, 2)]
print(f'Computer chose: {computer_choice}')

print(
    '\033[1;32mChoose an option:\033[m\n'
    '[0] - Rock\n'
    '[1] - Paper\n'
    '[2] - Scissors'
)
your_turn = int(input('Choose an option: '))
if your_turn in (0, 1, 2):
  your_choice = items[your_turn]

  if your_choice == computer_choice:
       print(
           "It's a tie!\n"
           f'Computer choice: {computer_choice}\n'
           f'You chose: {your_choice}'
       )

  elif (
           (your_choice == 'Rock' and computer_choice == 'Scissors') or
           (your_choice == 'Paper' and computer_choice == 'Rock') or
           (your_choice == 'Scissors' and computer_choice == 'Paper')
   ):
       print(
             'You win!\n'
             f'Computer chose: {computer_choice}\n'
             f'You chose: {your_choice}'
       )
  else:
      print('Computer wins!')

else:
    print('Choose a valid option!')