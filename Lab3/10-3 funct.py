def unique_elements(lst):
    seen = []
    for x in lst:
        if x not in seen:
            seen.append(x)
    return seen