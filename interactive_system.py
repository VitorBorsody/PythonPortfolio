

def grades_info(sit=False):

    l = list()
    while True:
        student_profile = dict()

        student_profile['name'] = str(input('Enter the name of the student: ')).strip().title()
        try:
            student_profile['grade'] = float(input(f'Enter grade from student: '))
        except ValueError:
            print('Please enter a numeric value! ')
            continue
        control_variable = str(input('Do you wish to continue [y/n]? ')).strip().lower()
        l.append(student_profile.copy())

        if not control_variable:
            print('Input cannot be empty! ')

        if control_variable not in ('n', 'y'):
            print('Please, enter either "n" or "y"')

        if control_variable[0] == 'n':
            break

    if sit:
        for student in l:
            if student['grade']>=7:
                student['Situation'] = 'Well done'
            elif 5<=student['grade']<7:
                student['Situation'] = 'Reasonable'
            else:
                student['Situation'] = 'Bad'
        print("\n Students situation: ")
        for student in l:
            print(f'{student["name"]} - {student["Situation"]}')





    if len(l)>0:
        grades = [student["grade"] for student in l]
        print(
            f'Total grades: {len(grades)}\n'
            f'Maximum grade: {max(grades)}\n'
            f'Minimum grade: {min(grades)}\n'
            f'Average grade: {sum(grades)/len(grades):.2f}'
        )

    return l




l = grades_info(sit=True)
