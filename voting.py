
def vote(year_of_birth:int):
    from datetime import datetime
    """
    Determines voting status based on year of birth
    :param year_of_birth: Year of birth of the person
    :type year_of_birth: int
    :return: voting status
    :rtype: str
    """
    current_year = datetime.now().year
    age = current_year - year_of_birth
    if  16<age<65:
        print(
            f'You are {age} years old!\n'
            'Mandatory voting!'

        )
    elif age>65:
        print(
            f'You are {age} years old\n'
            f' Optional voting!'
        )
    else:
        print(
            f'You are {age} years old\n'
            f'Vote denied!'
        )

vote(2009)
