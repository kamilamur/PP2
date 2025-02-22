import re
def split_at_uppercase(text):
    result = re.findall(r'[A-Z][a-z]*', text)
    return result
input_string = input("string: ")
output_list = split_at_uppercase(input_string)
print("Split string:", output_list)