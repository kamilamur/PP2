import re
def replace_characters(text):
    pattern = r'[ ,.]'
    result = re.sub(pattern, ':', text)
    return result
input_string = input("string: ")
output_string = replace_characters(input_string)
print("Modified:", output_string)