import re
def match_string(text):
    pattern = r'^ab{2,3}$'
    if re.match(pattern, text):
        return "Match found! "
    else:
        return "No match!"
input_string = input("string: ")
result = match_string(input_string)
print(result)