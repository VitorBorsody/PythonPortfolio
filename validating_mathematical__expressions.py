expression = str(input('Enter a mathematical expression: '))
# Store all the open parentheses
stack = []
for char in expression:
    if char == '(':
        stack.append(char) #push
    elif char == ')':
        if not stack:
            print('Invalid expression! ')
            break
        else:
            stack.pop() #pop

# The for loop's else block only executes if the loop completes without a break

else:
    if not stack:
        print('Valid expression! ')
    else:
        print('Invalid expression! ')


