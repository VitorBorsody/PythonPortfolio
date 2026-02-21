
data = []
while True:
  k = float(input('Please enter a number: '))
  data.append(k)
  control_variable = input('Enter 999 if you want to exit. Otherwise press enter: ')

  if control_variable == '999':
      break

print(
    f'How many values were entered? {len(data)}\n'
    f"What's the sum of these values? {sum(data)}"
)