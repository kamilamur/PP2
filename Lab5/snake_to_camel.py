def snake_to_camel(snake_str):
    components = snake_str.split('_')
    camel_str = components[0] + ''.join(x.capitalize() for x in components[1:])
    return camel_str
input_string = input("snake_case string: ")
output_string = snake_to_camel(input_string)
print("camelCase string:", output_string)