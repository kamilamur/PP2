import re
def match_string(text):
    pattern = r'^ab*$'
    if re.match(pattern, text):
        return "Match found! "
    else:
        return "No match!"
input_string = input("Enter a string: ")
result = match_string(input_string)
print(result)