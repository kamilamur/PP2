import re
def insert_spaces(text):
    result = re.sub(r'(?<!^)([A-Z])', r' \1', text)
    return result
input_string = input("a CamelCase string: ")
output_string = insert_spaces(input_string)
print("Modified string:", output_string)