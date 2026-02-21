from datetime import date
year_of_birth= int(input('Enter your year of birth: '))
current_age = date.today().year - year_of_birth

if current_age < 18:
    k="year" if 18-current_age == 1 else "years"
    print(
        f'There are {18-current_age} {k} left before military enlistment'
    )
elif current_age > 18:
    k="year" if current_age - 18 == 1 else "years"
    print(f'You should have enlisted {current_age-18} {k} ago')
else:
    print(f'You have to report to the army immediately!!!')