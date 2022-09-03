import re
def get_number_from_string(string):
    ints = ""
    ints_str = '0123456789'
    for char in string:
        if char in ints_str:
            ints += char
    return ints


print(get_number_from_string("Hell1o Worl2d1"))