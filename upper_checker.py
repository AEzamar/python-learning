def is_uppercase(inp):
    upper_count = 0
    for char in inp:
        if char == char.upper():
            upper_count += 1
    if upper_count == len(inp):
        return True
    else: 
        return False


print(is_uppercase("THIS IS A STRING MANG"))


def upper_checker1(inp):
    for char in inp:
        char != char.upper()


print(upper_checker1("THIS IS A STRiNG"))