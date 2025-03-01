def check_all_true(tpl):
    return all(tpl)
example_tuple = (True, 1, "non-empty", [1, 2, 3])
result = check_all_true(example_tuple)
print("All elements are true:", result)