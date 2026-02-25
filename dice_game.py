from random import randint
from time import sleep
from operator import itemgetter

play = {
    'player1': randint(1, 6),
    'player2': randint(1, 6),
    'player3': randint(1,6),
    'player4': randint(1, 6)
}
ranking = list()
print('Drawn values: ')
for key, value in play.items():
    print(f'{key} got a {value} on the dice')
    print('Processing...')
    sleep(1)

# Order by value not by key
ranking = sorted(play.items(), key=itemgetter(1), reverse = True)
print(ranking)
for i, v in enumerate(ranking):
    if i == 0:
      k = 'st'
      print(f'{i + 1}{k} place: {v[0]} who rolled a {v[1]} ')
    if i == 1:
        k = 'nd'
        print(f'{i + 1}{k} place: {v[0]} who rolled a {v[1]}')
    if i == 2:
        k = 'rd'
        print(f'{i + 1}{k} place: {v[0]} who rolled a {v[1]} ')
    if i == 3:
        k = 'th'
        print(f'{i + 1}{k} place: {v[0]} who rolled a {v[1]}')


