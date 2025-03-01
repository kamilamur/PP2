def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

input_string = input("string: ")
if is_palindrome(input_string):
    print("string is a palindrome.")
else:
    print("string isn't a palindrome.")