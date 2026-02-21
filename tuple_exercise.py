from random import randint
#1
count = ("zero", "one", "two", "three", "four")

while True:
    n = str(input('Enter a number between [zero, four]: ')).strip().lower()
    if n in count:
        print(f'You entered: {n}')
        break
    else:
        print(f'Enter a valid number between [Zero, Four] ')

#2 Football teams

football_teams = ("Corinthians", "Palmeiras", "Santos", "Chapecoense", "Vasco", "Bahia")

# The top five teams

for i in range(0, 6):
    print(football_teams[i], end = ' ')
print()

# The last four teams in the standings
last_four = football_teams[-4:]
for teams in last_four:
    print(teams, end = ' ')
print()

# Sorted teams
sorted_teams = sorted(football_teams)
print(sorted_teams)

# What position is Chapecoense in?

position_in_the_standings = football_teams.index("Chapecoense") + 1
print(f"Chapecoense's Position in the standings: {position_in_the_standings}°")

# Random numbers
drawn_numbers = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(drawn_numbers)
maximum_value = max(drawn_numbers)
minimum_value = min(drawn_numbers)
print(f'Maximum value: {maximum_value}')
print(f'Minimum value: {minimum_value}')

# Data analysis using a tuple

values = ()
even_numbers = ()
for i in range(0, 5):
    n = float(input('Enter a number: '))
    values += (n,)
    if n % 2 == 0:
        even_numbers += (n,)

print(f'How many times did the number 9 appear? {values.count(9)}')
print(f'At what position did the number 3 appear for the first time? {values.index(3)}')
print(f'Which numbers were even? {even_numbers}')
print(values)

# OR (more professional):

temp = []

for i in range(0,5):
    n1 = float(input('Enter a number: '))
    temp.append(n1)
k = tuple(temp)
print(k)
