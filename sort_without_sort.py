temp = []
min_value = None
c = 0
for _ in range(5):
    try:
        n=float(input('Enter a number: '))
    except ValueError:
        print('Enter a number! ')
        continue
    if not temp:
        temp.append(n)
    else:
        inserted = False
        for i in range(len(temp)):
            if n < temp[i]:
                temp.insert(i, n)
                inserted = True
                break
        if not inserted:
            temp.append(n)
print(temp)