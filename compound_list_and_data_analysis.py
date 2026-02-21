temp = []
data = []
registration_count = 0
heaviest = None
lightest = None
heaviest_person_name = ''
lightest_person_name = ''


while True:

    temp.append(str(input("What's your name?")))
    try:
        temp.append(float(input("What's your weight? ")))
    except ValueError:
        print('Invalid input! Please try again!')
        continue

    data.append(temp[:])
    temp.clear()

    for i in range(0, len(data)):
        if heaviest is None or heaviest < data[i][1]:
            heaviest = data[i][1]
            heaviest_person_name = data[i][0]
        if lightest is None or lightest > data[i][1]:
            lightest = data[i][1]
            lightest_person_name = data[i][0]

    control_variable = str(input('Would you like to continue (y/n)? ')).strip().lower()
    if not control_variable:
        print('Enter a valid option! ')
        continue
    control_variable = control_variable[0]
    if control_variable not in ('y', 'n'):
        print("Enter either 'y' or 'n'! ")
        continue
    if control_variable == 'n':
        break

print(f'The heaviest person is {heaviest_person_name} and weighs {heaviest} kg')
print(f'The lightest person is {lightest_person_name} and weighs {lightest} kg')
print(f'How many users were registered? {len(data)}')