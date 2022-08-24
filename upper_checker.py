def is_uppercase(inp):
    upper_count = 0
    for char in inp:
        if char == char.upper():
            upper_count += 1
    print(upper_count, len(inp))
    if upper_count == len(inp):
        return True
    else: 
        return False



print(is_uppercase("THIS IS A STRING MANG"))