pattern_form = list()
while True:

  name = str(input('Name: '))
  grade1 = float(input('Grade1: '))
  grade2 = float(input('Grade2: '))
  average = (grade1+grade2)/2
  pattern_form.append([name, [grade1, grade2], average])
  print(pattern_form)
  control_variable = str(input('Continue? [y/n]: ')).strip().lower()
  if not control_variable:
      print('Input cannot be empty!!')
      continue
  if control_variable not in ('y', 'n'):
      print('Enter either y or n!!')
      continue
  if control_variable == 'n':
        break
print('-='*45)
print(f'{"Index":<15}{"Name":<15}{"Average":>8}')
print('-'*45)
for i, a in enumerate(pattern_form):
    print(f'{i:<15}{a[0]:<15}{a[2]:>8.1f}')