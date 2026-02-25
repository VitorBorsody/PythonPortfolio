from datetime import datetime
a = dict()
a['name'] = str(input('Name: '))
while True:
 try:
    a['work card'] = int(input("Work card (enter 0 if you don't have one): "))
    a['birthdate'] = int(input("What's your date of birth? "))
    break
 except ValueError:
    print('Invalid input! ')


age = datetime.now().year - a['birthdate']
if a['work card'] != 0:
    a['year of employment'] = int(input("Year of employment: "))
    a['salary'] = float(input('Salary: '))
    print(
        f'You are {age} years old\n'
        f'There are {2065-a["year of employment"]} years left until retirement! '
    )


