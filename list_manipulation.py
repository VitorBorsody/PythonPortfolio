list_items = []
values = list(range(0, 10))
values[0]=1
values.append(11)
values.sort(reverse=True)
values.pop(0)
values.insert(9, 0)
print(values)
if 25 in values:
    values.remove(25)
else:
    print('Value not in list')
print(f'This list has {len(values)} elements')

for index, value in enumerate(values):
    print(f'Index {index} -> {value} ')

for _ in range(0, 5):
    n = int(input('Enter a value: '))
    list_items.append(n)
list_items.sort(reverse=True)
print(list_items)

# Creating a copy of a list

a = [1, 2, 3]
b = a[:]
b[2]=10
print(a)
print(b)



temp = []

for i in range(0, 5):
    z = float(input(f'Enter a value for index {i}: '))
    temp.append(z)
    if temp[i]==max(temp):
       maximum_value = max(temp)
       print(
           f'Maximum value: {maximum_value}\n'
           f'Index: {temp.index(maximum_value)}'
       )
    elif temp[i]==min(temp):
       minimum_value = min(temp)
       index_min = temp.index(minimum_value)
       print(
           f'Minimum value: {minimum_value}\n'
           f'Index: {temp.index(minimum_value)}'
             )
    else:
        print(
            f'Value: {temp[i]}\n'
            f'Index: {temp.index(i)}'
        )
print(temp)