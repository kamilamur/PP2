import re
def camel_to_snake(camel_str):
    snake_str = re.sub(r'(?<!^)([A-Z])', r'_\1', camel_str).lower()
    return snake_str
input_string = input("a CamelCase string: ")
output_string = camel_to_snake(input_string)
print("snake_case string:", output_string)