from random import choice, shuffle
# Ramdomly selected students
students_drawn = ["Vitor", "Lucas", "Carlos", "John"]
print('The chosen student is: {} '.format(choice(students_drawn)))

# Presentation order

students = []

for i in range(1,5):
    name = input(f"Enter the name of student {i}: ")
    students.append(name)
shuffle(students)

print(students)