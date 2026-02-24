from random import sample
game_list = []

number_of_attempts = int(input('How many games would you like to generate? '))

for i in range(number_of_attempts):
    drawn_numbers = sample(range(1,61), 3)
    drawn_numbers.sort()
    game_list.append(drawn_numbers)

print(f'The numbers drawn were: {game_list}')