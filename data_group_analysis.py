M = 0
F_under20 = 0
users_over18 = 0

print(
    '[M] - Male\n'
    '[F] - Female'
)
while True:


  gender = str(input('Enter your gender: ')).strip().upper()
  try:
      age = int(input("Enter your age: "))

  except ValueError:
      print('Please, enter an integer number')
      continue
  if gender == 'M':
      M += 1
  if gender == 'F' and age < 20:
      F_under20 += 1

  if age >= 18:
      users_over18 += 1

  if gender not in ('M', 'F'):
      print('Please enter either M or F')
      continue

  control_variable=str(input('Would you like to continue [y/n]? ')).lower().strip()[0]
  if not control_variable:
      print('Please enter either M or F')
  if control_variable[0] not in ('y', 'n'):
      print('Please enter either y or n')
      continue
  if control_variable[0] == 'n':
      break

k1='is' if M==1 else 'are'
k2='is' if users_over18==1 else 'are'
k3='is' if F_under20==1 else 'are'

print(
    f'There {k1} {M} male individual(s) in the dataset!\n'
    f'There {k2} {users_over18} individual(s) over 18 years old!\n'
    f'There {k3} {F_under20} female individual(s) in the dataset!\n'
)



