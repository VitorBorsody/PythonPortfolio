from random import randint
wins = 0
while True:
    computer_choice = randint(0, 10)
    choice = str(input('Even or Odd? ')).strip().capitalize()
    if choice not in ('Even', 'Odd'):
        print('Invalid input! Choose either even or odd. ')
        continue

    try:
        your_turn = int(input('Enter a number within the interval [0, 10] '))
        if your_turn < 0 or your_turn > 10:
            print("It's outside the interval [0, 10]")
            continue
    except ValueError:
        print("Enter just an integer number")
        continue
    s = computer_choice + your_turn
    print(f'The computer chose: {computer_choice}')
    print(f'Your choice: {your_turn}')
    print(f'Sum of the numbers: {s}')
    if s%2 == 0:
        result = 'Even'
        print("It's even!")
    else:
        result = 'Odd'
        print("It's odd")

        if result == choice:
            wins += 1
            print('You won!')
            print(f'Your winning streak is: {wins}')
        else:
            print('You lost!')
            print(f'Total winning streak is: {wins}')
            break
print('End of the game!')

