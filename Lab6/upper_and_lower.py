def count_upper_lower(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count
input_string = input("string: ")
upper_count, lower_count = count_upper_lower(input_string)
print("number of uppercase letters:", upper_count)
print("number of lowercase letters:", lower_count)