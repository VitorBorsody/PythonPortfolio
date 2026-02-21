names = []
ages = []
genders = []
c_male = 0
c_female = 0
c_ageF = 0
oldest_male_name = ''
oldest_male_age = -1
print(
    'Male - M\n'
    'Female - F'
)
for i in range(1, 3):

    name = str(input('Please enter your name: ')).strip().lower().capitalize()
    age = int(input('Please enter your age: '))
    while True:
      gender = str(input('Please enter your gender: ')).strip().upper()
      if gender in ('M', 'F'):
          break
      print('Invalid input, please try again!')

    names.append(name)
    ages.append(age)
    genders.append(gender)

    if gender == 'M':
        c_male += 1
    elif gender == 'F':
        c_female += 1

    if gender == 'F' and age<20:
        c_ageF += 1

    if gender == 'M' and age>oldest_male_age:
        oldest_male_age = age
        oldest_male_name = name





average_age = sum(ages)/len(ages)

print(
   f'The average age of the group is: {average_age:.2f}'

)
if c_ageF>1:
    print(
    f'There are {c_ageF} females under 20 years old'
    )
elif c_ageF ==1:
    print(
        f'There is {c_ageF} female under 20 years old'
    )
else:
    print('There are no females under 20 years old')
if oldest_male_age != -1:
    print(
    f'The name of the oldest man is: {oldest_male_name}\nHe is {oldest_male_age} years old'
    )
else:
    print('There are no men in the group!')


