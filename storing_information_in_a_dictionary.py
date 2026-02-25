data = dict()
k = list()
for _ in range(0, 2):
    try:
      data['Name'] = str(input('Name: '))
      data['Average'] = float(input('Average: '))
    except ValueError:
      print('Please enter a numeric value! ')
      break
    if data['Average'] < 6:
        data['Situation'] = 'Failed'
    else:
        data['Situation'] = 'Passed'
    k.append(data.copy())
print()
# Get all students
for student in k:
# Get only the last student
 for key, value in data.items():
    print(f' - {key}:{value}\n')
print('-*'*30)

