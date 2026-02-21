# is it a palindrome or not?

phrase = str(input("Enter the phrase to verify if it's a palindrome or not: ")).strip().lower()
inverted_phrase = phrase[::-1]
if phrase == inverted_phrase:
    print('Palindrome')
else:
    print("It isn't a palindrome!")