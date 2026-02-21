n1 = float(input('Enter the first grade: '))
n2 = float(input('Enter the second grade: '))
average_grade = (n1+n2)/2
if average_grade>=7.0:
    print(
        'Well done! You passed the exam!\n'
        'You scored: {} points'.format(average_grade)
    )

elif 5<=average_grade<=6.9:
    print(
        'You need to take the remedial exam!\n'
        'You scored: {} points'.format(average_grade)
)

elif average_grade<5:
    print(
        'You failed the exam!\n'
        f'You scored {average_grade} points '
          )