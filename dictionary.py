# Creating a dictionary

data = dict()

# Returning values in the dictionary

data = {'name': 'Vitor', 'age': 25}

print(data['age'])

# Including new categories:

data['gender'] = 'M'

print(data['gender'])

# removing...

del data['name']

print(data.values())
print(data.keys())
print(data.items())

print('-='*30)

for k, v in data.items():
    print(f'{k}:{v}')

print('-='*30)

for k in data.keys():
    print(f'{k}:{data[k]}')

print('-='*30)

for v in data.values():
    print(f'{v}')

print('-='*30)

country = []
s1 = {'State':'São Paulo', 'State abbreviation': 'SP'}
s2 = {'State': 'RJ', 'State abbreviation': 'RJ'}
country.append(s1)
country.append(s2)
print(country[0]['State'])
print(country[1]['State'])

# The list stores copies of the dictionary in each iteration

a = dict()
b = list()

for c in range(0, 2):
    a["State"] = str(input('State: '))
    a["State abbreviation"] = str(input('State code: '))
    b.append(a.copy())
print(b)
print('-='*30)


for s in b:
    for k, v in s.items():
        print(f'The field {k} has value {v} ')