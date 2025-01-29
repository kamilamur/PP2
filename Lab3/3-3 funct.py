def solve(num_heads, num_legs):
    for num_chickens in range(num_heads + 1):
        num_rabbits = num_heads - num_chickens
        if 2 * num_chickens + 4 * num_rabbits == num_legs:
            return num_chickens, num_rabbits
    return None, None