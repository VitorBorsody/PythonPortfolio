def factorial(n:int):
    """
    Factorial function that returns the factorial of a given number!
    :param n: factorial you'd like to calculate...
    :type n: int
    :return: factorial of n!
    :rtype: NoneType
    """
    c=n
    f=1
    print(f'Calculating {n}!=', end = '')
    while c>0:
        print(c, end = '')
        print('x' if c>1 else '=', end = '')
        f *=c
        c-=1
    print(f, end = ' ')
    

factorial(5)

help(factorial)