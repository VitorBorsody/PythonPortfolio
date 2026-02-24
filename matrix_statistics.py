even_numbers = []
third_column = []
second_row = []
biggest_value = None

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for row in range(0, 3):
    for col in range(0, 3):
        try:
          matrix[row][col] = int(input(f'Enter a number for [{row}, {col}]: '))
        except ValueError:
            print('Enter an integer number! ')
            continue
        if matrix[row][col] % 2 == 0:
            even_numbers.append(matrix[row][col])
        # Or:
        # for row in range(0,3):
        # col_sum += matrix[row][2]

        if col == 2:
            third_column.append(matrix[row][col])
        # Or:
        # for col in range(0,3):
        # row_sum += matrix[1][col]

        if row == 1:
            second_row.append(matrix[row][col])
        if row == 1:
           if biggest_value is None or biggest_value < matrix[1][col]:
              biggest_value = matrix[row][col]

for row in range(0,3):
    for col in range(0,3):
        print(f'[{matrix[row][col]:^5}]', end = '')
    print()

print(
    f'Sum of even numbers: {sum(even_numbers)}\n'
    f'Sum of third column: {sum(third_column)}\n'
    f'Sum of second row: {sum(second_row)}\n'
    f'Maximum value in the second row: {biggest_value}'
)

