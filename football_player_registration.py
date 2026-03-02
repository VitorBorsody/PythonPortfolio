player = dict()
matches = list()

number_of_matches = int(input('Enter the number of matches: '))
while True:
    player['name'] = str(input('Enter the name of the soccer player: ')).strip().title()

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
    control_variable = str(input('Do you wish to continue (Y/N)?')).strip().capitalize()
    if not control_variable:
        print('Input cannot be empty! ')
        continue
    if control_variable[0] not in ('Y', 'N'):
        print("Enter either 'Y' or 'N'! ")
        continue
    if control_variable[0] == 'N':
        break





