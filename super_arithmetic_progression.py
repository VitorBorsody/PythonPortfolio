a1 = float(input("Enter the first term of the AP:  "))
d1 = float(input("Enter the common difference: "))
n = 1
additional_terms = 10
initial_term = 10
for _ in range(initial_term):

    an = a1 + (n - 1) * d1
    print(f'{an}', end = '')
    print(' - ' if n<10 else ' ', end = '')

    n += 1

while True:
    additional_terms = int(input("\nHow many additional terms would you like to display?"))
    if additional_terms == 0:
      print('Program finished!')
      break

    for i in range(additional_terms):
      an = a1 + (n-1)*d1
      n += 1
      if i < additional_terms - 1:
          print(an, end = ' - ')
      else:
          print(an)

