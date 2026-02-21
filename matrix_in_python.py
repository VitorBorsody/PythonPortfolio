matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for row in range(0, 3):
    for col in range(0, 3):
        try:
          matrix[row][col] = int(input(f'Enter a number for [{row}, {col}]: '))
        except ValueError:
            print('Enter a number! ')
            continue

for row in range(0, 3):
    for col in range(0, 3):
        print(f'[{matrix[row][col]:^5}]', end = ' ')
    print()

