import re
def string_clean(s):
    return re.sub("[0-9]", "\s", s)


print(string_clean("Ohh12 dang112 mang"))