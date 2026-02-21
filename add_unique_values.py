temp = []

while True:
    try:
        n = int(input('Enter an integer number: '))
    except ValueError:
        print("Please, enter an integer number!")
        continue
    if n not in temp:
            temp.append(n)
    else:
            print('Already there!')
            continue
    control_variable = str(input('Do you wish to continue [y/n]? ')).strip().lower()

    if not control_variable:
        print("Input cannot be empty!")
        continue
    control_variable = control_variable[0]
    if control_variable not in ('y', 'n'):
        print('Please, enter either "y" or "n"!')
        continue
    if control_variable == 'n':
        break


sorted_list=sorted(temp)
print(sorted_list)

