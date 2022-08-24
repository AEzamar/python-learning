def is_uppercase(inp):
    for char in inp:
        if char != char.upper():
            return False
        else:
            return True


print(is_uppercase("THIS IS A STRING MANg"))