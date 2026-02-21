from datetime import date
birth_year= int(input("What year were you born?"))
current_year = date.today().year
athlete_age = current_year - birth_year
k="years" if athlete_age>1 else "year"
print(f"You are {athlete_age} {k} old")
if athlete_age < 10:
    print("You are U10")
elif 10<=athlete_age < 15:
    print("You are U14")
elif 15<=athlete_age<20:
    print("You are U19")
elif 19<athlete_age<=25:
    print("You are Senior")
else:
    print("You are Master")
