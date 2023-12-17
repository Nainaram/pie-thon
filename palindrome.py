def is_palindrome(word):
   # cleaned_word = word
   #.join() is  a string method used to concatenete  a string
   # .isalnum() is a method that checks whether a entered are all alphanumerical or not
   #.lower is method that converts all the string characters into lower case
    cleaned_word = ''.join(c.lower() for c in word if c.isalnum())
    return cleaned_word == cleaned_word[::-1]

user_input = input("Enter a word or phrase to check for palindrome: ")
if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
