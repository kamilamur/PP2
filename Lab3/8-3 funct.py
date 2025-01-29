def spy_game(nums):
    pattern = [0, 0, 7]
    index = 0
    for num in nums:
        if num == pattern[index]:
            index += 1
            if index == len(pattern):
                return True
    return False