# obs: Declaring personal_info inside the while loop would eliminate the need for .copy(). It would be enough to write: "personal_info_list.append(personal_info)"

personal_info = dict()
personal_info_list = list()
total_age = 0
greater_than_average_age = list()
women_list = list()

print(
    'Male - [M]\n'
    'Female - [F]'
)
while True:

    personal_info['name'] = str(input('Enter your name: ')).title().strip()
    personal_info['gender'] = str(input('Enter your gender: [M/F] ')).strip().upper()
    try:
      personal_info['age'] = int(input('Enter your age: '))
    except ValueError:
        print('Please enter a valid age! ')
        continue
    if personal_info['gender'] not in ('M', 'F'):
        print('Please enter either M or F')
        continue
    control_variable = str(input('Do you wish to continue? [Y/N] ')).strip().upper()
    personal_info_list.append(personal_info.copy())

    if personal_info['gender'] == 'F':
        women_list.append(personal_info.copy())


    if not control_variable:
        print('Input cannot be empty! ')
        continue
    if control_variable[0] == 'N':
        break
    if control_variable[0] not in ('Y', 'N'):
        print('Enter a valid option! ')

print(f'Number of people: {len(personal_info_list)}')

for person in personal_info_list:
    total_age += person['age']
if personal_info_list:
  average_age = total_age / len(personal_info_list)

else:
    average_age = 0

print(f'Women list: {women_list}')

for person in personal_info_list:
    if person['age']>average_age:
        greater_than_average_age.append(person)
print(f'List with ages greater than average: {greater_than_average_age}')
