# 01

# name = input('Enter your name: ')
#
# uppercase_name = name.upper()
# lowercase_name = name.lower()
# print(f"""
# Name length without space: {len(name.replace(' ', ''))}\n
# Uppercase name: {uppercase_name}\n
# Lowercase name: {lowercase_name}\n
# How many letters does the first name have? {len(name.split()[0])}
#       """
#       )
#
# # 02
# number = int(input('Enter a number: '))
# if 0<=number<=9999:
#
#  units = number // 1 % 10
#  tens = number // 10 % 10
#  hundreds = number // 100 % 10
#  thousands = number // 1000 % 10
#
#  print(
#        f"Units: {units}\n"
#        f"Tens: {tens}\n"
#        f"Hundreds: {hundreds}\n"
#        f"Thousands: {thousands}\n"
#  )
# else:
#       print("Invalid number")
#
# # 03
#
# city = str(input('Enter a city:')).strip().title()
# if city[:5] == 'Santo':
#       print("A cidade começa com 'Santo' ")
# else:
#       print("A cidade não começa com 'Santo'")
#
# # 04
#
# name_Silva = str(input('Enter a name: ')).title().strip()
# # if name_Silva.find('Silva')!= -1:
# #       print('It contains Silva')
# # else:
# #       print('It does not contain Silva')
#
# if 'Silva' in name_Silva:
#       print('It contains Silva')
# else:
#       print('It does not contain Silva')

# 05

# phrase = str(input('Enter a phrase: ')).upper()
#
# print(
# f"How many times does the letter A appeared?: {phrase.count('A')}\n"
# f"At what position does it first appear?: {phrase.find('A')}\n"
# f"At what index does it last appear?: {phrase.rfind('A')}"
# )

# 06

lastANDfirst_name = str(input('Enter your full name:')).strip()
l = lastANDfirst_name.split()
last_name = l[-1]
print(
f"First name: {lastANDfirst_name.split()[0]}\n"
f"Last name/Surname:  {last_name}\n"
)
