c1 = 0
c2 = 0
n = int(input('How many people would you like to verify? '))
def ordinal(k):
    if 10 <= k % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(k % 10, "th")
    return f"{k}{suffix}"

for i in range(1, n+1):

    age = int(input(f"What's the age of the {ordinal(i)} person?"))
    if age < 18:
        c1 += 1
    else:
        c2 += 1

z1 = 'person' if c1 == 1 else 'people'
z2 = 'person' if c2 == 1 else 'people'

print(
    f"{c1} {z1} under 18 years old\n"
    f"{c2} {z2} of legal age"
)
