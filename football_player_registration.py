player = dict()
matches = list()
player['name'] = str(input('Enter the name of the soccer player: '))
number_of_matches = int(input('Enter the number of matches: '))

for i in range(0, number_of_matches):
    matches.append(int(input(f'How many goals were scored in match {i+1}? ')))
player['goals'] = matches[:]
player['total'] = sum(matches)
print('-='*30)
for key, value in player.items():
  print(f'{key}:{value}')
print('-='*30)
print(f'Player {player["name"]} played {len(player["goals"])} matches')
for i, v in enumerate(player['goals']):
    print(f'In match {i+1}, scored {v} goals')
print(f'Total goals: {player["total"]}')


